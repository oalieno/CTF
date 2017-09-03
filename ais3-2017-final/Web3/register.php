<?php
require_once('class.php');
if(isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if(strlen($username) < 3 or strlen($username) > 16)
        die('Invalid user name');

    if(strlen($password) < 3 or strlen($password) > 16)
        die('Invalid password');
    if(!$user->is_exists($username)) {
        $user->register($username, $password);
        echo 'Register OK!<a href="index.php">Please Login</a>';
    }
    else {
        die('User name Already Exists');
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
        <form action="register.php" method="post" class="well" style="width:220px;margin:0px auto;">
            <h3>Register</h3>
            <label>Username:</label>
            <input type="text" name="username" style="height:30px"class="span3"/>
            <label>Password:</label>
            <input type="password" name="password" style="height:30px" class="span3">

            <button type="submit" class="btn btn-primary">REGISTER</button>
        </form>
    </div>
</body>
</html>
<?php
}
?>
