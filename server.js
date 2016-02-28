// vendor library
var passport = require('passport');
var bcrypt = require('bcrypt-nodejs');
var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');
var session = require('express-session');
var ejs = require('ejs');
var LocalStrategy = require('passport-local').Strategy;

// custom library
// model
var Model = require('./database/model');
var functions = require('./functions');

var express = require('express');
/*var pdf2json = require('pdf2json');*/
var router = express.Router();
var app = express();

passport.use(new LocalStrategy(function(username, password, done) {
    new Model.User({username: username}).fetch().then(function(data) {
        var user = data;
        if(user === null) {
            return done(null, false, {message: 'Invalid username or password'});
        } else {
            user = data.toJSON();
            if(!bcrypt.compareSync(password, user.password)) {
                return done(null, false, {message: 'Invalid username or password'});
            } else {
                return done(null, user);
            }
        }
    });
}));

passport.serializeUser(function(user, done) {
    done(null, user.username);
});

passport.deserializeUser(function(username, done) {
    new Model.User({username: username}).fetch().then(function(user) {
        done(null, user);
    });
});

var dbConfig = {
    client: 'mysql',
    connection: {
        host: 'localhost',
        user: 'root',
        password: 'your_password',
        database: 'blog',
        charset: 'utf8'
    }
};

//var knex = require('knex')(dbConfig);
//var bookshelf = require('bookshelf')(knex);
//app.set('bookshelf', bookshelf);
app.use(cookieParser());
app.use(bodyParser());
app.use(session({secret: 'secret strategic xxzzz code'}));
app.use(passport.initialize());
app.use(passport.session());

/*Variables to make things easier to read*/
var port = 8080;
var path = __dirname + '/public/views/';


/*Express App Routing*/
app.use("/",require('./routes'));
app.use("*",function(req,res){
    res.sendFile(path + "404.html");
});
app.listen(port, function () {
    console.log('listening on port '+ port);
});

