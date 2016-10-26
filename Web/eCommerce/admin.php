<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="./styles/style.css" />
    <title>Light Music Event • Section Admin</title>
</head>

<body>
    <div id="main-wrapper">
        <?php include("header.php") ?>

        <main>
            <aside id="side-options">
            </aside>
        
            <ul id="section-title-nav">
                <li class="section-title-active">Section Admin</li>                
            </ul>
        
            <section id="main-content">
                <form id="connexion-admin" action="#">
                    <label>Email</label>
                    <input type="text" value="">
                    <br />

                    <label>Mot de passe</label>
                    <input type="text" value="">
                    <br />
                
                    <input class="envoyer" type="submit" value="Connexion">
                </form> 
            </section>  
        </main>
    </div>
</body>
</html>