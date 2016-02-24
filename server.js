var express = require('express');
var pdf2json = require('pdf2json');
var path = require('path');

var app = express();
var port = 8080;

app.get('/', function (request, response) {
    response.sendFile(path.join(__dirname, '/views', 'index.html'));
});

app.post('/upload', function (request, response) {
    response.send('test');
});

app.listen(port, function () {
    console.log('listening on port '+ port);
});
