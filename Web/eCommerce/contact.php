<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="./styles/style.css" />
    <title>Light Music Event • Inscription</title>
</head>

<body>
    

    <div id="main-wrapper">
        <?php include("header.php") ?>


    <main>
        <aside id="side-options">
        </aside>
        
        <ul id="section-title-nav">
            <li class="section-title-active">Nous contacter</li>            
        </ul>
        
        <section id="main-content">
            <form id="nous-contacter" action="#">
                <label>Titre</label>
                <input class="titre" type="text" value="">
                <br />

                <label>Objet</label>
                <input class="objet" type="text" value="">
                <br />
                
                <label>Message</label>
                <input class="message" type="text" value="">
                <br />

                <input class="envoyer" type="submit" value="Envoyer">
            </form> 
        </section>  
    </main>
    </div>
</body>
</html>