<?php
	$servername = "mysql.cs.iastate.edu";
	$username = dbu309grp17;
	$password = AugtUmP22JP;
	$database = db309grp17;
	$conn = new mysqli($servername, $username, $password, $database);
	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}
?>