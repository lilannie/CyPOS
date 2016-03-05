<ul class="list-group">
      <?php
            while ($row = mysqli_fetch_assoc($result)){
                  foreach ($row as $key => $value) {
                        if ($key == 'acronym')
                              echo "<li class='list-group-item'><a href='/classes/classes.php?major=$value'>";
                        if ($key == 'name')
                              echo "$value</a></li>"; 
                  }
            }
      ?>
</ul>