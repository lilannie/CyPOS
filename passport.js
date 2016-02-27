//loads what is necessary
var LocalStrategy = require('passport-local').Strategy;

//load user
var express = require('express');
var mysql = require('mysql');
var passport = require('passport');
var config = {
        host: 'mysql.cs.iastate.edu',  // your host
        user: 'dbu309grp17', // your database user
        password: 'AugtUmP22JP', // your database password
        database: 'db309grp17',
        charset: 'UTF8_GENERAL_CI'
    };


app.use(passport.initilize());
app.use(passport.session());

module.exports = function (passport, repository){

}

passport.serializeUser(function(user, done) {
    done(null, user.id);
});

passport.deserializeUser(function(user, done) {
    done(null, user);
});