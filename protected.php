<?php
session_start();

// Define the password
$correctPassword = 'yourPassword'; // Change this to your desired password

// Check if the form is submitted
if (isset($_POST['password'])) {
    if ($_POST['password'] === $correctPassword) {
        $_SESSION['loggedin'] = true; // Set session variable for logged-in status
    } else {
        $error = "Incorrect password. Please try again.";
    }
}

// If the user is not logged in, show the login form
if (!isset($_SESSION['loggedin']) || !$_SESSION['loggedin']) {
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Protected Page</title>
</head>
<body>
    <h2>Please enter the password:</h2>
    <form method="POST">
        <input type="password" name="password" required>
        <button type="submit">Submit</button>
    </form>
    <?php if (isset($error)) echo "<p style='color:red;'>$error</p>"; ?>
</body>
</html>
<?php
} else {
    // If logged in, show protected content
    echo "<h1>Protected Content</h1>";
    echo "<p>This is the content that is password protected.</p>";
    echo "<a href='logout.php'>Logout</a>";
}
?>
