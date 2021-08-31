<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */



define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'newbase');
 
/* Attempt to connect to MySQL database */
$link = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
 
// Check connection
if ($link->connect_error) {
    die("Connection failed: " . $link->connect_error);
}

$name = "";
$lastname= "";
$email= "";
$password = "";
$option = "";
$update = false;

if (isset($_POST['save'])) {
    $name = $_POST['name'];
    $lastname = $_POST['lastname'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $option = $_POST['option'];

   // mysqli_query"INSERT INTO user (firstname,lastname,email,company_h) VALUES ('$name','$lastname','$email','$option');
    $sql = "INSERT INTO user (firstname,lastname,password,email,company_h) VALUES ('$name','$lastname','$password','$email','$option')";

    if ($link->query($sql) === TRUE) {
        echo "New record created successfully";

      } else {
        echo "Error: " . $sql . "<br>" . $link->error;
        
    }

    header('location: user_table.php');
}

if (isset($_POST['submit'])) {
    $name = $_POST['name'];
    $host = $_POST['host'];
    $username = $_POST['username'];
    $password = $_POST['password'];
    $port = $_POST['port'];
    $path = $_POST['path'];
    $option = $_POST['option'];

   // mysqli_query"INSERT INTO user (firstname,lastname,email,company_h) VALUES ('$name','$lastname','$email','$option');
    $sql = "INSERT INTO serverinfo (name,host,username,password,port,path,status) VALUES ('$name','$host','$username','$password','$port','$path','$option')";

    if ($link->query($sql) === TRUE) {
        echo "New record created successfully";

      } else {
        echo "Error: " . $sql . "<br>" . $link->error;
        
      }


    $command = escapeshellcmd('python C:/Users/Soulaimane/Desktop/Automatic_Backup_System-master/Back-end/listconf.py 2>&1');
    $output = shell_exec($command);
    echo $output;
    
    
    $command = escapeshellcmd('python C:\Users\Soulaimane\Desktop\Automatic_Backup_System-master\Back-end\PingingSystem\pinging.py');
    $output = shell_exec($command);
    echo $output;




    header('location: server_table.php');

    $command = escapeshellcmd('python C:\Users\Soulaimane\Desktop\Automatic_Backup_System-master\Back-end\PingingSystem\pinging.py');
    $output = shell_exec($command);
    echo $output;
}


if (isset($_POST['addwebsite'])) {
  $name = $_POST['name'];
  $path = $_POST['path'];
  $url = $_POST['url'];
  $option = $_POST['option'];

  $sql = "INSERT INTO sitewebinfo (server_name,url_website,site_name,directory_path) VALUES ('$option','$url','$name','$path')";

  if ($link->query($sql) === TRUE) {
      echo "New record created successfully";

    } else {
      echo "Error: " . $sql . "<br>" . $link->error;
      
  }

  $command = escapeshellcmd('python C:\Users\Soulaimane\Desktop\Automatic_Backup_System-master\Back-end\PingingSystem\pinging.py');
  $output = shell_exec($command);
  echo $output;

  $command = escapeshellcmd('python C:\Users\Soulaimane\Desktop\Automatic_Backup_System-master\Back-end\PingingSystem\pinging.py');
  $output = shell_exec($command);
  echo $output;

  header('location: website_table.php');
}

if (isset($_POST['backup'])) {
  $checkbox1 = $_POST['customCheck'];
  $chk="";
  $m = $_POST['minute'];
  $h = $_POST['hour'];
  $dm = $_POST['day_m'];
  $mo = $_POST['month'];
  $dw = $_POST['day_w'];
  $txt = "minute : $m , hour : $h , day of month : $dm , month : $mo , day of week : $dw";

  echo ($txt);

  foreach($checkbox1 as $chk1)  
  {
    $sql = "SELECT server_name FROM sitewebinfo WHERE site_name='".$chk1."'";
    $result = mysqli_query($link, $sql);

    if (mysqli_num_rows($result) > 0) {
      $row = mysqli_fetch_assoc($result);
      $cc = $row['server_name'];
      $sqle = "INSERT into back_up (name,type,server_name,minute,hour,day_Month,Month,day_Week,status) VALUES('$chk1','WEBSITE','$cc','$m','$h','$dm','$mo','$dw','False')";
      if ($link->query($sqle) === TRUE) {
        echo "New record created successfully";
  
      } else {
        echo "Error: " . $sqle . "<br>" . $link->error;   
    }
    
    } else{
      $sql = "INSERT into back_up (name,type,minute,hour,day_Month,Month,day_Week,status) VALUES('$chk1','SERVER','$m','$h','$dm','$mo','$dw','False')";
      if ($link->query($sql) === TRUE) {
        echo "New record created successfully";
  
      } else {
        echo "Error: " . $sql . "<br>" . $link->error;
    }
    } 
  }

  $command = escapeshellcmd('python C:\Users\Soulaimane\Desktop\Automatic_Backup_System-master\Back-end\crontab\cron.py');
  $output = shell_exec($command);
  echo $output;


  header('location: backup_add.php');

  }

?>