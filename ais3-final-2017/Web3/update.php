<?php
require_once('class.php');
if(!isset($_SESSION['username'])) {
    die('Login First');
}
if(isset($_POST['phone']) && isset($_POST['email']) && isset($_POST['nickname']) && isset($_FILES['photo'])) {

    $username = $_SESSION['username'];
    if(!preg_match('/^\d{10}$/', $_POST['phone']))
        die('Invalid phone');

    if(!preg_match('/^[_a-zA-Z0-9]{1,10}@[_a-zA-Z0-9]{1,10}\.[_a-zA-Z0-9]{1,10}$/', $_POST['email']))
        die('Invalid email');

    if(preg_match('/[^a-zA-Z0-9_]/', $_POST['nickname']) || strlen($_POST['nickname']) > 10)
        die('Invalid nickname');

    $file = $_FILES['photo'];
    if($file['size'] < 5 or $file['size'] > 1000000)
        die('Photo size error');

    move_uploaded_file($file['tmp_name'], 'upload/' . md5($file['name']));
    $profile['phone'] = $_POST['phone'];
    $profile['email'] = $_POST['email'];
    $profile['nickname'] = $_POST['nickname'];
    $profile['photo'] = 'upload/' . md5($file['name']);

    $user->update_profile($username, serialize($profile));
    echo 'Update Profile Success!<a href="profile.php">Your Profile</a>';
}
else {
?>
<!DOCTYPE html>
<html>
<head>
   <title>UPDATE</title>
   <link href="static/bootstrap.min.css" rel="stylesheet">
   <script src="static/jquery.min.js"></script>
   <script src="static/bootstrap.min.js"></script>
</head>
<body>
    <div class="container" style="margin-top:100px">
        <form action="update.php" method="post" enctype="multipart/form-data" class="well" style="width:220px;margin:0px auto;"> 
            <h3>Please Update Your Profile</h3>
            <label>Phone:</label>
            <input type="text" name="phone" style="height:30px"class="span3"/>
            <label>Email:</label>
            <input type="text" name="email" style="height:30px"class="span3"/>
            <label>Nickname:</label>
            <input type="text" name="nickname" style="height:30px" class="span3">
            <label for="file">Photo:</label>
            <input type="file" name="photo" style="height:30px"class="span3"/>
            <button type="submit" class="btn btn-primary">UPDATE</button>
        </form>
    </div>
</body>
</html>
<?php
}
?>
