<?php
	include '../files/header.php';
	include '../files/connect.php';
	include '../query/se.php';
?>
	<div class="seClasses">
		<?php
			while ($row = mysqli_fetch_assoc($result)){
				foreach ($row as $key => $value) {
					if ($key == 'number')
						echo "<strong>$value : ";
					if ($key == 'name')
						echo "$value</br>";
					if ($key == 'Description')
						echo "Course Description:</strong></br>$value</br></br>";
				}
			}
		?>
	</div>
<?php 
	include '../files/footer.php';
?>