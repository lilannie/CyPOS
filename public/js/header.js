var header = "" +
    "<nav class='navbar navbar-default'>" +
    "<div class='container-fluid'>" +
    "<!-- Brand and toggle get grouped for better mobile display -->" +
    "<div class='navbar-header'>" +
    "<button type='button' class='navbar-toggle collapsed' data-toggle='collapse' data-target='#bs-example-navbar-collapse-1' aria-expanded='false'>" +
    "<span class='sr-only'>Toggle navigation</span>" +
    "<span class='icon-bar'></span>" +
    "<span class='icon-bar'></span>" +
    "<span class='icon-bar'></span>" +
    "</button>" +
    "<a class='navbar-brand' href='./home'>CyPOS</a>" +
    "</div>" +
    "<!-- Collect the nav links, forms, and other content for toggling -->" +
    "<div class='collapse navbar-collapse' id='bs-example-navbar-collapse-1'>" +
    "<ul class='nav navbar-nav'>" +
    "<li><a href='./new'>Generate New</a></li>" +
    "<li><a href='./view'>View POS</a></li>" +
    "<li><a href='./classes'>Classes</a></li>" +
    "</ul>" +
    "<form class='navbar-form navbar-left' role='search'>" +
    "<div class='form-group'>" +
    "<input type='text' class='form-control' placeholder='Search'>" +
    "</div>" +
    "<button type='submit' class='btn btn-default'>Submit</button>" +
    "</form>" +
    "<ul class='nav navbar-nav navbar-right'>" +
    "<li><a href='./logout'>Logout</a></li>" +
    "<li class='dropdown'>" +
    "<a href='./myaccount' class='dropdown-toggle' data-toggle='dropdown' role='button' aria-haspopup='true' aria-expanded='false'>My Account<span class='caret'></span></a>" +
    "<ul class='dropdown-menu'>" +
    "<li><a href='./manage'>Manage</a></li>" +
    "<li><a href='./history'>History</a></li>" +
    "<li role='separator' class='divider'></li>" +
    "<li><a href='./help'>Help</a></li>" +
    "</ul>" +
    "</li>" +
    "</ul>" +
    "</div><!-- /.navbar-collapse -->" +
    "</div><!-- /.container-fluid -->" +
    "</nav>";
document.write("");
$("body").before(header);

