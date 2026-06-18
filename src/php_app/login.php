<?php
/**
 * ⚠️ INTENTIONALLY VULNERABLE FILE ⚠️
 * Vulnerability: SQL Injection (Auth Bypass)
 * Description: Raw string concatenation in SQL query.
 * Secure Version: See src/secure_versions/secure_sql/prepared_statements.py
 */

require_once 'includes/db.php';
require_once 'includes/auth.php';

$error = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // VULNERABLE: Direct concatenation
    $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
    
    $result = $conn->query($sql);

    if ($result && $result->num_rows > 0) {
        $user = $result->fetch_assoc();
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        $_SESSION['role'] = $user['role'];
        header("Location: index.php");
        exit();
    } else {
        $error = "Invalid credentials. Query: " . $sql;
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>PHP Login - VulnArena</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <div class="warning-banner">⚠️ WARNING: INTENTIONALLY VULNERABLE PHP APP ⚠️</div>
    <div class="login-container">
        <h2>PHP Login Lab</h2>
        <?php if($error) echo "<p class='error'>$error</p>"; ?>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
