<?php
	include $_SERVER['DOCUMENT_ROOT'] . '/files/header.php';
	include $_SERVER['DOCUMENT_ROOT'] . '/files/connect.php';
	
	if (!is_null($_GET['major'])){
		include $_SERVER['DOCUMENT_ROOT'] . '/query/classes.php';
		include $_SERVER['DOCUMENT_ROOT'] . '/classes/majorTemplate.php';
	}
	else
		include $_SERVER['DOCUMENT_ROOT'] . '/query/departments.php';
		include $_SERVER['DOCUMENT_ROOT'] . '/classes/classesTemplate.php';

	include $_SERVER['DOCUMENT_ROOT'] . '/files/footer.php';
?>