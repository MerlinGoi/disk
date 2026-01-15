<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "komis";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
 die("Połączenie nieudane: " . $conn->connect_error);
}
echo "Połączenie udane!";


$sql = "SELECT * FROM t_samochody WHERE cena_wypozyczenia > 10000";
$result = $conn->query($sql);
while($row = $result->fetch_assoc()) {
 echo $row["marka"] . " - " . $row["cena_wypozyczenia"] . "<br>";
}


$sql = "SELECT * FROM t_wypozyczenia
 WHERE data_wypozyczenia BETWEEN '2025-05-01' AND '2025-05-31'";
$result = $conn->query($sql);
while($r = $result->fetch_assoc()) {
 echo $r["id_wypozyczenia"] . " - " . $r["data_wypozyczenia"] . "<br>";
}


$sql = "SELECT * FROM t_klienci WHERE telefon LIKE '6%'";
$r = $conn->query($sql);
while($k = $r->fetch_assoc()) {
 echo $k["nazwisko"] . " - " . $k["telefon"] . "<br>";
}


$sql = "SELECT * FROM t_samochody ORDER BY rok_produkcji DESC";
$r = $conn->query($sql);
while($s = $r->fetch_assoc()) {
 echo $s["marka"] . " - " . $s["rok_produkcji"] . "<br>";
}


$sql = "SELECT * FROM t_samochody ORDER BY cena_wypozyczenia DESC LIMIT 1";
$r = $conn->query($sql);
if($s = $r->fetch_assoc()) {
 echo "Najdroższy: " . $s["marka"] . " - " . $s["cena_wypozyczenia"];
}


$sql = "SELECT * FROM t_klienci WHERE nazwisko LIKE '%ski'";
$r = $conn->query($sql);
while($k = $r->fetch_assoc()) {
 echo $k["nazwisko"] . "<br>";
}


$sql = "SELECT AVG(cena_wypozyczenia) AS srednia FROM t_samochody";
$r = $conn->query($sql);
$row = $r->fetch_assoc();
echo "Średnia cena: " . $row["srednia"];


$sql = "SELECT *,
 DATEDIFF(data_zwrotu, data_wypozyczenia) AS dni
 FROM t_wypozyczenia";
$r = $conn->query($sql);
while($w = $r->fetch_assoc()) {
 echo "ID: " . $w["id_wypozyczenia"] .
 " — czas: " . $w["dni"] . " dni<br>";
}


$sql = "SELECT s.*
 FROM t_samochody s
 LEFT JOIN t_wypozyczenia w
 ON s.id_samochodu = w.id_samochodu
 WHERE w.id_samochodu IS NULL";
$r = $conn->query($sql);
while($s = $r->fetch_assoc()) {
 echo $s["marka"] . " — nigdy niewypożyczony<br>";
}


$sql = "SELECT k.id_klienta, k.imie, k.nazwisko, COUNT(*) AS ile
 FROM t_wypozyczenia w
 JOIN t_klienci k ON w.id_klienta = k.id_klienta
 GROUP BY k.id_klienta
 ORDER BY ile DESC
 LIMIT 3";
$r = $conn->query($sql);
while($k = $r->fetch_assoc()) {
 echo $k["imie"] . " " . $k["nazwisko"] .
 " — wypożyczeń: " . $k["ile"] . "<br>";
}
$conn->close();
?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href=" ">
    <script src="script.php"></script>
</head>
<body>
    <script>
        // Your JavaScript code to connect with script.php
        fetch('script.php')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Process the data as needed
            })
            .catch(error => console.error('Error:', error));
    </script>
</body>
</html>