<?php
require_once('class.php');
if(!isset($_SESSION['username'])) {
    die('Login First');
}
$username = $_SESSION['username'];
$profile=$user->show_profile($username);
if($profile  == null) {
    header('Location: update.php');
}
else {
    $profile = unserialize($profile);
    $phone = $profile['phone'];
    $email = $profile['email'];
    $nickname = $profile['nickname'];
    $photo = base64_encode(file_get_contents($profile['photo']));
?>
<!DOCTYPE html>
<html>
<head>
   <title>Profile</title>
   <link href="static/bootstrap.min.css" rel="stylesheet">
   <script src="static/jquery.min.js"></script>
   <script src="static/bootstrap.min.js"></script>
</head>
<body>
    <div class="container" style="margin-top:100px">
        <img src="data:image/gif;base64,<?php echo $photo; ?>" class="img-memeda " style="width:180px;margin:0px auto;">
        <h3>Hi <?php echo $nickname;?></h3>
        <label>Phone: <?php echo $phone;?></label>
        <label>Email: <?php echo $email;?></label>
    </div>
</body>
</html>
<?php
}
?>
