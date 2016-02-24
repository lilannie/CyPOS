var express = require('express');
var pdf2json = require('pdf2json');
var router = express.Router();

var path = __dirname + '/public/views/';
var app = express();
var port = 8080;

router.get("/",function(req,res){
    res.sendFile(path + "index.html");
});

router.get(/home/,function(req,res){
    res.sendFile(path + "home.html");
});

router.get("/new",function(req,res){
    res.sendFile(path + "new.html");
});

app.use("/",router);
app.use(express.static('public'));

/*//Defining middleware to server static files
app.use('static', express.static('./node_modules/bootstrap'));*/

app.use("*",function(req,res){
    res.sendFile(path + "404.html");
});

app.listen(port, function () {
    console.log('listening on port '+ port);
});
