<?php
require "db.php";

$sql = "SELECT * FROM pacjenci";
$res = $conn->query($sql);
?>
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Pacjenci</title>
</head>
<body>
<h1>Lista pacjentów</h1>

<table border="1" cellpadding="8">
    <tr>
        <th>ID</th>
        <th>Imię</th>
        <th>Nazwisko</th>
        <th>Wiek</th>
    </tr>

    <?php
    if ($res && $res->num_rows > 0) {
        while($row = $res->fetch_assoc()) {
            echo "<tr>";
            echo "<td>".$row["id"]."</td>";
            echo "<td>".$row["imie"]."</td>";
            echo "<td>".$row["nazwisko"]."</td>";
            echo "<td>".$row["wiek"]."</td>";
            echo "</tr>";
        }
    } else {
        echo "<tr><td colspan='4'>Brak danych</td></tr>";
    }
    ?>

</table>

<br>
<a href="index.html">Powrót</a>
</body>
</html>
