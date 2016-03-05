var passport = require('passport'),
    express = require('express'),
    session     = require('express-session'),
    bodyParser  = require('body-parser'),
    app = express(),
    pdf2json = require('pdf2json');

/*Variables to make things easier to read*/
var port = 8080;
var path = __dirname + '/public/views/';

require('./passport.js')(passport);

//Used to send login information to server
app.use(bodyParser.urlencoded({
    extended : true
}));
app.use(bodyParser.json());

app.use(session(
    {
        secret            : '309grp17',
        resave            : true,
        saveUninitialized : true
    }
));

app.use(passport.initialize());
app.use(passport.session());

//Configure static-serving directory for js, css, client side react components
require('./routes.js')(app, passport, express);

app.use("*",function(req,res){
    res.sendFile(path + "404.html");
});
app.listen(port, function () {
    console.log('listening on port '+ port);
});

