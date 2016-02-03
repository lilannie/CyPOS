var express = require('express');
var pdf2json = require('pdf2json');
var app = express();

app.get('/', function (request, response) {
    response.send('test');
});

app.post('/upload', function (request, response) {
    response.send('test');
});

app.listen(8080, function () {
    console.log('listening...');
});