<?php
	include '../files/connect.php';
	$result = mysqli_query($conn, "SELECT Courses.number, Courses.name, Courses.Description FROM Courses WHERE Courses.number LIKE 'S E%'");
	if (!$result)
		echo 'There was an error ' . mysqli_error($conn);
?>