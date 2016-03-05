<?php 
	include $_SERVER['DOCUMENT_ROOT'] . '/files/connect.php';
	$sqlCourses = "SELECT id, number FROM Courses";
	$sqlDepartments = "SELECT id, acronym FROM Departments";
	$resultCourses = mysqli_query($conn, $sqlCourses);
	$resultDepartments = mysqli_query($conn, $sqlDepartments);
	$index = 0;
	$rowDepartments = mysqli_fetch_all($resultDepartments);
	$previousDepartment = $rowDepartments[$index][1];
	$sqlString = "INSERT INTO Courses (departmentID) VALUES ('" . $rowDepartments[$index][0] . "') WHERE Courses.id = 1";
	if (mysqli_query($conn, $sqlString))
		echo 'okay';
	else
		echo 'idiot' . mysqli_error();
	if (!$resultCourses)
		echo 'you are an idiot' . mysqli_error($conn);
	if (!$resultDepartments)
		echo 'you are an idiot' . mysqli_error($conn);
	while ($rowCourses = mysqli_fetch_assoc($resultCourses)){
		// var_dump($rowCourses['number']);
		// var_dump($previousDepartment);
		// var_dump(strstr($rowCourses['number'], $previousDepartment));
		// var_dump("'" . $rowDepartments[$index][0] . "'");
		// if (strstr($rowCourses['number'], $previousDepartment))
		// 	mysqli_query($conn, "INSERT INTO Courses (departmentID) VALUES ('" . $rowDepartments[$index][0] . "')");
		// else{
		// 	$index ++;
		// 	$previousDepartment = $rowDepartments[$index][1];
		// }
	}
?>