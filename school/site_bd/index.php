<?php
$host = "127.0.0.1";
$user = "root";
$pass = "";
$dbname = "trump pece givings"; // <-- CHANGE THIS

$conn = mysqli_connect($host, $user, $pass, $dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT * FROM `not pece country`";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {

    while ($row = mysqli_fetch_assoc($result)) {
        echo "ID: " . $row['ID'] . "<br>";
        echo "Name: " . $row['name'] . "<br>";
        echo "Capital: " . $row['Capital'] . "<br>";
        echo "<hr>";
    }

} else {
    echo "No data found";
}

mysqli_close($conn);
?>




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script type="module" src="script.js"></script>
</head>
<body>
    <h1>db:</h1>
</body>
</html>