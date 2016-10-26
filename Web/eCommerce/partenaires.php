<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="./styles/style.css" />
    <title>Light Music Event • Partenaires</title>
</head>

<body>
    <div id="main-wrapper">
        <?php include("header.php") ?>

        <main>
            <aside id="side-options">
                <?php 
            
                if (isset($_GET["partenaire"]))
                {
                    switch ($_GET["partenaire"])
                    {
                        case "province de liège":
                            include("partenaires/province-liege.php");
                            break;
                    
                        case "nrj":
                            include("partenaires/nrj.php");
                            break;
                    
                        case "heineken":
                            include("partenaires/heineken.php");
                            break;
                    
                        default:
                            break;            
                    }
                }
            
                ?>
            </aside>

            <ul id="section-title-nav">
                <li class="section-title-active">Partenaires</li>
            </ul>

            <section id="main-content">
                <ul id="gallerie">
                    <li class="partenaire"><a href="partenaires.php?partenaire=heineken"><img src="./images/partenaires-01.png" alt="Heineken" /></a></li>
                    <li class="partenaire"><a href="partenaires.php?partenaire=province de liège"><img src="./images/partenaires-02.png" alt="Province de Liège" /></a></li>
                    <li class="partenaire"><a href="partenaires.php?partenaire=nrj"><img src="./images/partenaires-03.png" alt="NRJ" /></a></li>
                </ul>
            </section>
        </main>
    </div>
</body>
</html>