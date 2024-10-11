<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #333;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
  transition: background-color 0.3s, opacity 0.3s;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #545454;
  color: white;
}

.menu-toggle {
  display: none;
  float: right;
  padding: 14px 16px;
  cursor: pointer;
  background: none;
  border: none;
  color: white;
  font-size: 24px;
}

@media screen and (max-width: 600px) {
  .topnav a {
    display: none;
  }
  .topnav a.active {
    display: block;
  }
  .topnav .menu-toggle {
    display: block;
  }
  .topnav.responsive {
    position: relative;
  }
  .topnav.responsive a {
    display: block;
    float: none;
  }
}
</style>
</head>
<body>

<div class="topnav" id="myTopnav">
  <a class="active" href="#home">Home</a>
  <a href="#news">News</a>
  <a href="#contact">Contact</a>
  <a href="#about">About</a>
  <button class="menu-toggle" onclick="toggleMenu()" aria-expanded="false" role="button">&#9776;</button>
</div>

<div style="padding-left:16px">
  <h2>Top Navigation Example</h2>
  <p>Some content..</p>
  
  <!-- Button to navigate to a different page -->
  <button onclick="navigateToPage()">Go to Another Page</button>
</div>

<script>
function toggleMenu() {
  var topnav = document.getElementById("myTopnav");
  var toggleButton = document.querySelector('.menu-toggle');
  if (topnav.className === "topnav") {
    topnav.className += " responsive";
    toggleButton.setAttribute('aria-expanded', 'true');
  } else {
    topnav.className = "topnav";
    toggleButton.setAttribute('aria-expanded', 'false');
  }
}

function navigateToPage() {
  // Replace 'another-page.html' with the actual URL you want to navigate to
  window.location.href = 'another-page.html';
}
</script>

</body>
</html>
