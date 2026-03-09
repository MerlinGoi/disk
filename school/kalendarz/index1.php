<?php
$host = "localhost";
$user = "root";
$pass = "";
$dbname = "kalendarz";

$conn = mysqli_connect($host, $user, $pass, $dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Get month and year from GET parameters, default to August 2020
$month = isset($_GET['month']) ? intval($_GET['month']) : 8;
$year = isset($_GET['year']) ? intval($_GET['year']) : 2020;

// Month names in Polish
$monthNames = [
    1 => 'styczen',
    2 => 'luty',
    3 => 'marzec',
    4 => 'kwiecien',
    5 => 'maj',
    6 => 'czerwiec',
    7 => 'lipiec',
    8 => 'sierpien',
    9 => 'wrzesien',
    10 => 'pazdziernik',
    11 => 'listopad',
    12 => 'grudzień'
];

$currentMonthName = $monthNames[$month];
$daysInMonth = date('t', mktime(0,0,0,$month,1,$year));

/* ADD NOTE */
if (isset($_POST['add_note'])) {

    $day = intval($_POST['day']);
    $note = mysqli_real_escape_string($conn, $_POST['note']);

    if ($day >= 1 && $day <= $daysInMonth && !empty($note)) {

        // Create full date for selected month and year
        $date = "$year-" . str_pad($month, 2, "0", STR_PAD_LEFT) . "-" . str_pad($day, 2, "0", STR_PAD_LEFT);

        $sql = "INSERT INTO zadania (dataZadania, wpis, miesiac, rok)
                VALUES ('$date', '$note', '$currentMonthName', $year)";

        mysqli_query($conn, $sql);
    }
}

/* GET NOTES FOR SELECTED MONTH */
$notes = [];
$result = mysqli_query($conn,
    "SELECT * FROM zadania WHERE miesiac='$currentMonthName' AND rok=$year"
);

while ($row = mysqli_fetch_assoc($result)) {
    $dayNumber = date("j", strtotime($row['dataZadania']));
    $notes[$dayNumber][] = $row['wpis'];
}
?>

<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Sierpniowy kalendarz</title>

<link rel="stylesheet" href="style.css">
</head>

<body>

<header>
<h1>Organizer: <?php echo strtoupper($currentMonthName) . ' ' . $year; ?></h1>

<div class="navigation">
    <a href="?month=<?php echo $month-1 < 1 ? 12 : $month-1; ?>&year=<?php echo $month-1 < 1 ? $year-1 : $year; ?>">Poprzedni miesiąc</a>
    <a href="?month=<?php echo $month+1 > 12 ? 1 : $month+1; ?>&year=<?php echo $month+1 > 12 ? $year+1 : $year; ?>">Następny miesiąc</a>
</div>

<form method="POST">
    <label>Dzień (1-<?php echo $daysInMonth; ?>):</label>
    <input type="number" name="day" min="1" max="<?php echo $daysInMonth; ?>" required>

    <label>Wydarzenie:</label>
    <input type="text" name="note" required>

    <button type="submit" name="add_note">Dodaj</button>
</form>
</header>

<section>

<?php
for ($i = 1; $i <= $daysInMonth; $i++) {

    echo "<div class='calendar-section'>";
    echo "<div class='day-number'>Dzień $i</div>";

    if (!empty($notes[$i])) {
        foreach ($notes[$i] as $n) {
            echo "<p>$n</p>";
        }
    }

    echo "</div>";
}
?>

</section>

<footer>Stronę stworzył: Jan Kowalski</footer>

</body>
</html>

<?php mysqli_close($conn); ?>