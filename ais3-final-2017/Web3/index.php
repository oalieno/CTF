<?php
require_once('class.php');
if(isset($_SESSION['username'])) {
    header('Location: profile.php');
    exit;
}
if(isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if(strlen($username) < 3 or strlen($username) > 16)
        die('Invalid user name');

    if(strlen($password) < 3 or strlen($password) > 16)
        die('Invalid password');

    if($user->login($username, $password)) {
        $_SESSION['username'] = $username;
        header('Location: profile.php');
        exit;
    }
    else {
        die('Invalid user name or password');
    }
}
else {
?>
<!DOCTYPE html>
<html>
<head>
   <title>Login</title>
   <link href="static/bootstrap.min.css" rel="stylesheet">
   <script src="static/jquery.min.js"></script>
   <script src="static/bootstrap.min.js"></script>
</head>
<body>
    <div class="container" style="margin-top:100px">
        <form action="index.php" method="post" class="well" style="width:220px;margin:0px auto;">
            <h3>Login</h3>
            <label>Username:</label>
            <input type="text" name="username" style="height:30px"class="span3"/>
            <label>Password:</label>
            <input type="password" name="password" style="height:30px" class="span3">

            <button type="submit" class="btn btn-primary">LOGIN</button>
		or <a href="register.php">register here</a>
        </form>
    </div>
</body>
</html>
<?php
}
?>
