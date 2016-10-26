<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="./styles/style.css" />
    <title>Light Music Event • List Participants</title>
</head>

<body>
    <div id="main-wrapper">
         <?php include("header.php") ?>

    <main>
        <aside id="side-options">
            <?php 
            
            if (isset($_GET["artiste"]))
            {
                switch ($_GET["artiste"])
                {
                    case "uppermost":
                        include("artistes/uppermost.php");
                        break;
                    
                    case "mitis":
                        include("artistes/mitis.php");
                        break;
                    
                    case "feint":
                        include("artistes/feint.php");
                        break;
                    
                    default:
                        break;            
                }
            }
            
            ?>
        </aside>
        
        <ul id="section-title-nav">
            <li class="section-title-active">Liste participants</li>
            <li class="section-title"><a href="./inscription.php">S'inscrire</a></li>
        </ul>
        
        <section id="main-content">
            <table id="artist-table">
                <tr class="artist">
                    <th class="rank">Rang</th>
                    <th class="name">Nom Artiste</th>
                    <th class="votes">Nombre votes</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td><a href="./participants.php?artiste=uppermost">Uppermost</a></td>
                    <td>1320<a href="" title="voter" class="vote-artist">Voter</a></td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><a href="./participants.php?artiste=mitis">MitiS</a></td>
                    <td>1152<a href="" title="voter" class="vote-artist">Voter</a></td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><a href="./participants.php?artiste=feint">Feint</a></td>
                    <td>1093<a href="" title="voter" class="vote-artist">Voter</a></td>
                </tr>
                <tr>
                    <td>4</td>
                    <td><a href="">Fox Stevenson</a></td>
                    <td>985<a href="" title="voter" class="vote-artist">Voter</a></td>
                </tr>
                <tr>
                    <td>5</td>
                    <td><a href="">Kill Paris</a></td>
                    <td>748<a href="" title="voter" class="vote-artist">Voter</a></td>
                </tr>
                <tr>
                    <td>6</td>
                    <td><a href="">Rameses B</a></td>
                    <td>523<a href="" title="voter" class="vote-artist">Voter</a></td>
                </tr>
                <tr>
                    <td>7</td>
                    <td><a href="">Porter Robinson</a></td>
                    <td>501<a href="" title="voter" class="vote-artist">Voter</a></td>
                </tr>
                <tr>
                    <td>8</td>
                    <td><a href="">Gavin G</a></td>
                    <td>422<a href="" title="voter" class="vote-artist">Voter</a></td>
                </tr>
                <tr>
                    <td>9</td>
                    <td><a href="">Blackmill</a></td>
                    <td>306<a href="" title="voter" class="vote-artist">Voter</a></td>
                </tr>
            </table>
        </section>  
    </main>
    </div>
</body>
</html>