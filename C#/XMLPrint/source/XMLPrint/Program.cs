using System;
using System.Collections.Generic;
using System.Xml;
using System.IO;
using Microsoft.Win32;

namespace XMLPrint
{
    class Program
    {
        [STAThread]
        static int Main(string[] args)
        {
            // --------------------------------------------------------------------------------------------------
            // 1. Création d'un tableau contenant les données pour la présentation
            // --------------------------------------------------------------------------------------------------
            // Fichier contenant les instructions pour la présentation des données
            string infosPresentationPath = String.Format("{0}\\{1}", AppDomain.CurrentDomain.BaseDirectory, "informations-intervention.xml");

            // Vérification de l'existence du fichier
            if (!File.Exists(infosPresentationPath))
                return (int)XMLPrintError.InformationsFileNotFound;

            // Chargement du document en mémoire
            XmlDocument infosPresentation = new XmlDocument();
            infosPresentation.Load(infosPresentationPath);

            // Création du tableau
            List<Dictionary<string, string>> XMLPresentation = new List<Dictionary<string, string>>();

            // --------------------------------------------------------------------------------------------------
            // a. On récupère pour chaque balise 'information', la valeur 'label', 'chemin-balise' et
            ///   'nom-attribut'. Toute balise 'information' n'ayant pas ces valeurs sera ignoré
            // --------------------------------------------------------------------------------------------------
            // Recherche dans la balise 'main' contenant toutes les informations nécessaires
            XmlNode mainNode = infosPresentation.SelectSingleNode("main");
            if (mainNode != null)
            {
                // On séléctione la balise 'information'
                XmlNodeList informationNode = mainNode.SelectNodes("information");
                // Recherche les balises suivantes à l'intérieur de la balise "information"
                string[] informationTags = { "label", "chemin-balise", "nom-attribut" };


                foreach (XmlNode information in informationNode)
                {
                    Dictionary<string, string> tempDictionary = new Dictionary<string, string>();

                    foreach (string tag in informationTags)
                    {
                        XmlNode temp = information.SelectSingleNode(tag);

                        if (temp != null)
                        {
                            tempDictionary.Add(temp.Name, temp.InnerText);
                        }
                        else
                        {
                            tempDictionary = null;
                            break;
                        }
                    }

                    if (tempDictionary != null)
                        XMLPresentation.Add(tempDictionary);
                }
            }
            // Si on ne trouve pas la balise "main" dans le fichier de paramètre XML
            // du programme, quitter le programme
            else
            {
                return (int)XMLPrintError.NoMainNode;
            }


            // --------------------------------------------------------------------------------------------------
            // 2. Création du fichier de présentation des informations
            // --------------------------------------------------------------------------------------------------
            // Le nom du fichier de présentation des informations
            string presentFileName = "presentation.html";
            // Le chemin vers le fichier de présentation des informations
            string presentFilePath = String.Format("{0}{1}", AppDomain.CurrentDomain.BaseDirectory, presentFileName);

            // --------------------------------------------------------------------------------------------------
            // 3. Récupération des données du fichier XML
            // --------------------------------------------------------------------------------------------------
            // Nom du fichier contenant les informations sur l'intervention
            if (args.Length == 0)
                return (int)XMLPrintError.NoParameters;

            // Vérification de l'existence du fichier
            if (!File.Exists(args[0]))
                return (int)XMLPrintError.InterventionFileNotFound;

            // On stocke le chemin vers le fichier d'intervention
            string infosInterventionPath = args[0];

            // Récupération des informations dans le fichier d'intervention
            XmlDocument infosIntervention = new XmlDocument();
            infosIntervention.Load(infosInterventionPath);

            // --------------------------------------------------------------------------------------------------
            // 4. Écriture des données sur le fichier de présentations des informations
            // --------------------------------------------------------------------------------------------------   
            using (StreamWriter file = new StreamWriter(presentFilePath))
            {
                // --------------------------------------------------
                // a. Écriture de l'en-tête HTML
                // --------------------------------------------------
                file.Write("<!DOCTYPE html><html><head><title>Présentation intervention</title>");
                file.Write("<meta charset=\"UTF-8\">");
                file.Write("<link rel=\"stylesheet\" href =\"style.css\" type=\"text/css\"></head><body>");

                file.Write("<h1>Informations intervention</h1>");

                file.Write("<table id='records'>");

                // --------------------------------------------------
                // b. Écriture contenu HTML
                // --------------------------------------------------
                // Pour chaque information qu'on doit récupèrer dans le fichier XML
                foreach (Dictionary<string, string> information in XMLPresentation)
                {
                    // Séléction des noeuds indiqués par le chemin
                    XmlNodeList occurrencesBalise = infosIntervention.SelectNodes(information["chemin-balise"]);
                    List<string> listeInformations = new List<string>();

                    // Si l'information ne doit pas être récupérée dans la valeur de l'attribut
                    if (information["nom-attribut"] == "")
                    {
                        foreach (XmlNode occurrence in occurrencesBalise)
                            listeInformations.Add(occurrence.InnerText);
                    }
                    // Si l'information doit être récupérée dans la valeur de l'attribut
                    else
                    {
                        foreach (XmlNode occurrence in occurrencesBalise)
                        {
                            // Si l'attribut existe
                            if (occurrence.Attributes[information["nom-attribut"]] != null)
                                listeInformations.Add(occurrence.Attributes[information["nom-attribut"]].Value);
                        }
                    }


                    // Si la liste des informations n'est pas vide
                    if (listeInformations.Count != 0)
                    {
                        // Écriture du label
                        file.Write(String.Format("<tr><td class='label'>{0} :</td><td class='values'>", information["label"]));

                        // Écriture des occurences
                        for (int i = 0; i < listeInformations.Count; i++)
                        {
                            if (i == listeInformations.Count-1)
                                file.Write(listeInformations[i]);
                            else
                                file.Write(String.Format("{0}<br />", listeInformations[i]));
                        }

                        file.Write("</td></tr>");
                    }
                }

                file.Write("</table>");

                // --------------------------------------------------
                // c. Écriture fermeture fichier HTML
                // --------------------------------------------------
                file.Write("</body></html>");
            }

            // --------------------------------------------------------------------------------------------------
            // 5. Impression du fichier HTML
            // --------------------------------------------------------------------------------------------------   
            // --------------------------------------------------------------------------------------------------
            // a. Éviter impression avec un paramètre d'execution du programme
            // --------------------------------------------------------------------------------------------------
            // Éviter l'impression en paramètre
            if (args.Length >= 2)
            {
                if (args[1] == "NoPrint" || args[1] == "noprint")                
                    return (int)XMLPrintError.NoPrint;                
            }

            // --------------------------------------------------------------------------------------------------
            // b. On enlève le header et footer imprimé par défaut par IE et on imprime
            // --------------------------------------------------------------------------------------------------
            string keyName = @"Software\Microsoft\Internet Explorer\PageSetup";
            using (RegistryKey key = Registry.CurrentUser.OpenSubKey(keyName, true))
            {
                if (key != null)
                {
                    Object oldFooter = key.GetValue("footer");
                    Object oldHeader = key.GetValue("header");
                    if (oldFooter != null)
                        key.SetValue("footer", "");
                    if (oldHeader != null)
                        key.SetValue("header", "");  

                    HTMLPrinter printer = new HTMLPrinter();
                    printer.Print(presentFilePath);

                    if (oldFooter != null)
                        key.SetValue("footer", oldFooter.ToString());
                    if (oldHeader != null)
                        key.SetValue("header", oldHeader.ToString());
                }
            }

            return (int)XMLPrintError.Successful;
        }

        private enum XMLPrintError
        {
            Successful = -1,
            NoParameters = 0,
            InformationsFileNotFound = 1,
            InterventionFileNotFound = 2,
            NoMainNode,
            NoInformationNode,
            NoPrint
        }

        // Fonction sur "thread" qui gère un objet d etype WebBrowser
        /*private static void RunFormThread(string fileToPrint)
        {
            // Création d'un formulaire pour utiliser l'objet de type WebBroswer
            Form myForm = new Form();
            myForm.ShowInTaskbar = false;
            myForm.Size = new System.Drawing.Size(0, 0);

            WebBrowser webBrowser = new WebBrowser();
            webBrowser.Url = new Uri(fileToPrint);
            webBrowser.DocumentCompleted += WebBrowser_OnDocumentCompleted;
            
            Application.Run(myForm);
        }

        // Se charge d'imprimer le fichier HTML lorsque le fichier est chargé
        private static void WebBrowser_OnDocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            ((WebBrowser)sender).Print();
        }*/

    }
}
