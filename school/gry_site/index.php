<?php
$conn = new mysqli("localhost", "root", "", "gry");
?>

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Gry komputerowe</title>
    <link rel="stylesheet" href="styl7.css">
</head>
<body>

<header>
    <h1>Ranking gier komputerowych</h1>
</header>

<main>
    <section class="lewa">
        <h3>Top 5 gier</h3>
        <ul>
            <?php

            $zapytanie1 = "SELECT nazwa, punkty FROM gry ORDER BY punkty DESC LIMIT 5";
            $wynik1 = $conn->query($zapytanie1);

            while($wiersz = $wynik1->fetch_assoc()){
                echo "<li>".$wiersz['nazwa']." <span class='punkty'>".$wiersz['punkty']."</span></li>";
            }
            ?>
        </ul>

        <h3>Nasz sklep</h3>
        <a href="http://sklep.gry.pl">Tu kupisz gry</a>

        <h3>Stronę wykonał</h3>
        <p>00000000</p>
    </section>

    <section class="srodek">
        <?php
        $zapytanie2 = "SELECT id, nazwa, zdjecie FROM gry";
        $wynik2 = $conn->query($zapytanie2);

        while($wiersz = $wynik2->fetch_assoc()){
            echo "<div class='gra'>";
            echo "<img src='".$wiersz['zdjecie']."' alt='".$wiersz['nazwa']."' title='".$wiersz['id']."'><br>";
            echo "<p>".$wiersz['nazwa']."</p>";
            echo "</div>";
        }
        ?>
    </section>

    <section class="prawa">
        <h3>Dodaj nową grę</h3>
        <form method="post">
            Nazwa: <input type="text" name="nazwa"><br>
            Opis: <input type="text" name="opis"><br>
            Cena: <input type="text" name="cena"><br>
            Zdjęcie: <input type="text" name="zdjecie"><br>
            <button type="submit" name="dodaj">DODAJ</button>
        </form>

        <?php
        if(!empty($_POST['nazwa'])){
            $nazwa = $_POST['nazwa'];
            $opis = $_POST['opis'];
            $cena = $_POST['cena'];
            $zdjecie = $_POST['zdjecie'];

            $zapytanie4 = "INSERT INTO gry(nazwa, opis, punkty, cena, zdjecie)
            VALUES('$nazwa','$opis',0,'$cena','$zdjecie')";

            $conn->query($zapytanie4);
            
        }
        ?>
    </section>
</main>

<footer>
    <?php
    if(!empty($_POST['id'])){
        $id = $_POST['id'];
        $zapytanie3 = "SELECT nazwa, opis, punkty, cena FROM gry WHERE id=$id";
        $wynik3 = $conn->query($zapytanie3);

        if($wiersz = $wynik3->fetch_assoc()){
            echo "<h2>".$wiersz['nazwa'].", ".$wiersz['punkty']." punktów, ".$wiersz['cena']." zł</h2>";
            echo "<p>".$wiersz['opis']."</p>";
        }
    }

    $conn->close();
     ?>
    <form method="post">
        <input type="text" name="id">
        <button type="submit" name="pokaz">Pokaż opis</button>
    </form>


</footer>

</body>
</html>
