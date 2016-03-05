<div class="major">
	<?php
		while ($row = mysqli_fetch_assoc($result)){
			foreach ($row as $key => $value) {
				if ($key == 'number')
					echo "<strong>$value : ";
				if ($key == 'name')
					echo "$value</br></strong>";
				if ($key == 'prereqs' && !is_null($value))
					echo "<i><strong>Prereqs: </strong></i>$value</br>";
				if ($key == 'description' && $value != "")
					echo "<strong>Course Description:</strong></br>$value</br></br>";
				else if ($key == 'description')
					echo "</br></br>"; 
			}
		}
	?>
</div>