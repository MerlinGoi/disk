<?php
// api.php - Secure backend for OpenAI API calls

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

// Your API key (keep secure - ideally in environment variable)
$API_KEY = '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';

// Handle preflight requests
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

// Only allow POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
    exit;
}

// Get JSON input
$input = json_decode(file_get_contents('php://input'), true);

if (!isset($input['message']) || empty(trim($input['message']))) {
    http_response_code(400);
    echo json_encode(['error' => 'Message is required']);
    exit;
}

$userMessage = trim($input['message']);

// Prepare request to OpenAI API
$url = 'https://api.openai.com/v1/chat/completions';
$headers = array(
    'Content-Type: application/json',
    'Authorization: Bearer ' . $API_KEY
);

$data = array(
    'model' => 'gpt-3.5-turbo',
    'messages' => array(
        array('role' => 'user', 'content' => $userMessage)
    ),
    'temperature' => 0.7,
    'max_tokens' => 500
);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_TIMEOUT, 30);

$response = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// Forward the response
http_response_code($http_code);
echo $response;
?>
