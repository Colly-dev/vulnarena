<?php
require_once 'includes/db.php';
session_start();

$results = [];
if (isset($_GET['q'])) {
    $q = $_GET['q'];
    // VULNERABLE: SQL Injection
    $sql = "SELECT id, username, email FROM users WHERE username LIKE '%$q%'";
    $result = $conn->query($sql);
    if ($result) {
        while($row = $result->fetch_assoc()) {
            $results[] = $row;
        }
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>PHP Search - VulnArena</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <div class="warning-banner">⚠️ WARNING: INTENTIONALLY VULNERABLE PHP APP ⚠️</div>
    <h2>Search Users</h2>
    <form method="GET">
        <input type="text" name="q" placeholder="Search..." value="<?php echo isset($_GET['q']) ? $_GET['q'] : ''; ?>">
        <button type="submit">Search</button>
    </form>

    <?php if ($results): ?>
        <table>
            <tr><th>ID</th><th>Username</th><th>Email</th></tr>
            <?php foreach($results as $row): ?>
                <tr>
                    <td><?php echo $row['id']; ?></td>
                    <td><?php echo $row['username']; ?></td>
                    <td><?php echo $row['email']; ?></td>
                </tr>
            <?php endforeach; ?>
        </table>
    <?php endif; ?>
</body>
</html>
