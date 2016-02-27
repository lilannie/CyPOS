var LocalStrategy = require('passport-local').Strategy;
    express = require('express');
    mysql = require('mysql';)
    passport = require('passport');
    config = {
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