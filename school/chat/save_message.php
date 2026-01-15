<?php
$host = "localhost";
$dbname = "chat";   // <-- change to your database name
$user = "root";
$pass = "";

try {
    // connect to database
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    echo "Connected successfully<br>";

    // insert data
    $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
    $stmt->execute(["Alice", "alice@example.com"]);

    echo "New record created successfully";

} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}
?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Simple Chat</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <h2>Simple Chat (logs messages to DB)</h2>
  <div id="chat" aria-live="polite"></div>

  <form id="form">
    <input id="message" type="text" autocomplete="off" placeholder="Type a message..." required />
    <button type="submit">Send</button>
  </form>

  <script src="script.js"></script>
</body>
</html>
