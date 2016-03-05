<?php
	include $_SERVER['DOCUMENT_ROOT'] . '/files/connect.php';
	$result = mysqli_query($conn, "SELECT Departments.acronym, Departments.name FROM Departments");
	if (!$result)
		echo 'There was an error ' . mysqli_error($conn);
?>