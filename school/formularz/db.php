<?php
$host = "localhost";      // lub 127.0.0.1
$user = "user";       // Twój użytkownik z uprawnieniami do bazy
$pass = "";               // Hasło jeśli jest ustawione
$db   = "przychodnia";    // nazwa bazy

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Błąd połączenia: " . $conn->connect_error);
}
?>
