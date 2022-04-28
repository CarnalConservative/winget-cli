<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // collect value of input field
  $firstname = $_POST['first_name'];
  
  $last_name = $_POST['last_name'];
  
  $performance = $_POST['performance'];
  
  $location = $_POST['location'];
  
  $room = $_POST['room'];
  
  $time_slot = $_POST['time_slot'];

  }
  $newEntry = "$firstname $lastname will be performing a $performance at the $location in room $room at $time_slot"
  
 
$file = 'Data.txt';
// The new person to add to the file
$entry = $newEntry;

file_put_contents($file, $entry, FILE_APPEND | LOCK_EX);

?>