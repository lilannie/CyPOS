// vendor library
var passport = require('passport');
var bcrypt = require('bcrypt-nodejs');

// custom library
// model
var Model = require('./database/model');

var express = require('express');
/*var pdf2json = require('pdf2json');*/
var router = express.Router();
var app = express();
/*var dbConfig = {
    client: 'mysql',
    connection: {
        host: 'localhost',
        user: 'root',
        password: 'your_password',
        database: 'blog',
        charset: 'utf8'
    }
};
app.set('bookshelf', bookshelf);

var knex = require('knex')(dbConfig);
var bookshelf = require('bookshelf')(knex);*/

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
