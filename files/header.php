<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>CyPos</title>
        <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.3/angular.min.js"></script>
	    <script src="//cdnjs.cloudflare.com/ajax/libs/angular.js/1.3.3/angular-route.min.js"></script>
	    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
	    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
	    <link rel="stylesheet" href="/css/main.css">
    </head>
    <body>
		<nav class="navbar navbar-default">
		    <div class="container-fluid">
		        <!-- Brand and toggle get grouped for better mobile display -->
		        <div class="navbar-header">
		            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
		                <span class="sr-only">Toggle navigation</span>
		                <span class="icon-bar"></span>
		                <span class="icon-bar"></span>
		                <span class="icon-bar"></span>
		            </button>
		            <a class="navbar-brand" href="/index.php">CyPOS</a>
		        </div>

		        <!-- Collect the nav links, forms, and other content for toggling -->
		        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
		            <ul class="nav navbar-nav">
		                <li <?php if ($_SERVER['REQUEST_URI'] == '/new.php') echo "class = active" ?> ><a href="/new.php">Generate New<span class="sr-only">(current)</span></a></li>
		                <li <?php if ($_SERVER['REQUEST_URI'] == '/view.php') echo "class = active" ?> ><a href="/view.php">View POS</a></li>
		                <li <?php if (strstr($_SERVER['REQUEST_URI'], "classes")) echo "class = active" ?> ><a href="/classes/classes.php">Classes</a></li>
		            </ul>
		            <form class="navbar-form navbar-left" role="search">
		                <div class="form-group">
		                    <input type="text" class="form-control" placeholder="Search">
		                </div>
		                <button type="submit" class="btn btn-default">Submit</button>
		            </form>
		            <ul class="nav navbar-nav navbar-right">
		                <li><a href="/">Logout</a></li>
		                <li class="dropdown">
		                    <a href="./myaccount" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My Account<span class="caret"></span></a>
		                    <ul class="dropdown-menu">
		                        <li><a href="/manage.php">Manage</a></li>
		                        <li><a href="/history.php">History</a></li>
		                        <li role="separator" class="divider"></li>
		                        <li><a href="/help.php">Help</a></li>
		                    </ul>
		                </li>
		            </ul>
		        </div><!-- /.navbar-collapse -->
		    </div><!-- /.container-fluid -->
		</nav>