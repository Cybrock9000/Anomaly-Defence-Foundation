<?php
session_start();
session_destroy(); // End the session
header("Location: protected.php"); // Redirect to the protected page
exit();
?>
