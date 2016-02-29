var router  =   require('express').Router()
var express =   require('express');
var path    =   __dirname + '/public/views/';
var functions = require('./functions');

/*//Sign In
//Get
//Called from app.js
var signIn = function(req, res, next) {
    if(req.isAuthenticated()) res.redirect('/');
    res.render('signin', {title: 'Sign In'});
};

// route middleware that will happen on every request
router.use(function(req, res, next) {
    // log each request to the console
    console.log(req.method, req.url);
    // continue doing what we were doing and go to the route
    next();
});*/

/*Basic Routes*/
router.get("/", function(req, res){
    res.sendFile(path + "index.html");
});
router.get("/home",function(req,res){
    res.sendFile(path + "home.html");
});
router.get("/classes",function(req,res){
    res.sendFile(path + "classes.html");
});
router.get("/help",function(req,res){
    res.sendFile(path + "help.html");
});
router.get("/history",function(req,res){
    res.sendFile(path + "history.html");
});
router.get("/home",function(req,res){
    res.sendFile(path + "home.html");
});
router.get("/manage",function(req,res){
    res.sendFile(path + "manage.html");
});
router.get("/myaccount",function(req,res){
    res.sendFile(path + "myaccount.html");
});
router.get("/new",function(req,res){
    res.sendFile(path + "new.html");
});
router.get("/view",function(req,res){
    res.sendFile(path + "view.html");
});

router.use(express.static(__dirname + '/public'));

module.exports = router;