<?php
	include $_SERVER['DOCUMENT_ROOT'] . '/files/connect.php';
	$queryString = htmlspecialchars($_GET['major']) . "%";
	$result = mysqli_query($conn, "SELECT Courses.number, Courses.name, Courses.prereqs, Courses.description FROM Courses WHERE Courses.number LIKE '$queryString'");
	if (!$result)
		echo 'There was an error ' . mysqli_error($conn);
?>