<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>PHP Dashboard - VulnArena</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <div class="warning-banner">⚠️ WARNING: INTENTIONALLY VULNERABLE PHP APP ⚠️</div>
    <nav>
        <a href="index.php">Dashboard</a> | 
        <a href="search.php">Search</a> | 
        <a href="upload.php">Upload</a> | 
        <a href="logout.php">Logout</a>
    </nav>
    <h1>Welcome, <?php echo $_SESSION['username']; ?></h1>
    <p>This is the PHP side of the VulnArena lab.</p>
</body>
</html>
