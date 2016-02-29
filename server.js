// vendor library
var passport = require('passport'),
    express = require('express'),
    session     = require('express-session'),
    bodyParser  = require('body-parser'),
    app = express(),
    pdf2json = require('pdf2json'),
    server      = require('http').Server(app),
    io          = require('socket.io')(server),
    knex        = require('knex')(module.exports = {
        client     : 'mysql',
        connection : {
            host     : 'mysql.cs.iastate.edu',
            user     : 'dbu309grp17',
            password : 'AugtUmP22JP',
            database : 'db309grp17',
            charset  : 'utf8'
        }
    }),
    Bookshelf   = require('bookshelf')(knex),
    Models      = require('./database/model')(Bookshelf),
    Collections = require('./database/collections')(Models, Bookshelf),
    repository  = require('./repository')(Models, Collections);

/*Variables to make things easier to read*/
var port = 8080;
var path = __dirname + '/public/views/';

//Initial database setup
repository.getAllUsers()
    .then(function (users) {
        if (users.length == 0) {
            repository.createUser('Annie', 'annie1')
        } else {
            console.log('Database is already set up');
        }
    });

//Settings for Passport (authentication)
require('./passport.js')(passport, repository);
app.use(passport.initialize());
app.use(passport.session());


/*Express App Routing*/
/*app.use("/",require('./routes')(express, path));*/

//Routes
require('./routes.js')(app, passport, io, repository, express);

//Configure static-serving directory for js, css, client side react components
app.use('/static', express.static(__dirname + '/public'));


app.use("*",function(req,res){
    res.sendFile(path + "404.html");
});
app.listen(port, function () {
    console.log('listening on port '+ port);
});

