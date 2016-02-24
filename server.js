var express = require('express');
var pdf2json = require('pdf2json');
var router = express.Router();

var path = __dirname + '/views/';
var app = express();
var port = 8080;

router.use(function (req,res,next) {
    console.log("/" + req.method);
    next();
});

router.get("/",function(req,res){
    res.sendFile(path + "index.html");
});

app.use("/",router);

app.use("*",function(req,res){
    res.sendFile(path + "404.html");
});

app.listen(port, function () {
    console.log('listening on port '+ port);
});
