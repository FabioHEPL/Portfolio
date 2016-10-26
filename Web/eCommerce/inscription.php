<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="./styles/style.css" />
    <title>Light Music Event • Nous Contacter</title>
</head>

<body>
    <div id="main-wrapper">
        <?php include("header.php") ?>

        <main>
            <aside id="side-options">
            </aside>
        
            <ul id="section-title-nav">
                <li class="section-title"><a href="./participants.php">Liste participants</a></li>
                <li class="section-title-active">S'inscrire</li>
            </ul>
        
            <section id="main-content">
                <form id="inscription-participant" action="#">
                    <label>Nom groupe</label>
                    <input type="text" value="">
                    <br />

                    <label>Genre</label>
                    <input type="text" value="">
                    <br />
                
                    <label>Email</label>
                    <input type="text" value="">
                    <br />

                    <label>Image</label>
                    <input type="file" accept="image/*">

                    <input class="envoyer" type="submit" value="Envoyer">
                </form> 
            </section>  
        </main>
    </div>
</body>
</html>