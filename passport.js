// load all the things we need
var LocalStrategy   = require('passport-local').Strategy;

var users = [
    {
        username: 'Annie',
        password: 'annie1'
    },
    {
        username: 'Rockie',
        password: 'rockie1'
    },
    {
        username: 'George',
        password: 'george1'
    },
    {
        username: 'Jens',
        password: 'jens1'
    }
];

// expose this function to our app using module.exports
module.exports = function(passport) {

    // used to serialize the user for the session
    passport.serializeUser(function(user, done) {
        for (var i = 0; i < users.length; i++) {
            if (user.username === users[i].username) {
                done(null, i);
            }
        }
    });

    passport.deserializeUser(function(id, done) {
        done(null, users[id]);
    });

    passport.use('login',
        new LocalStrategy({
                usernameField     : 'username',
                passwordField     : 'password',
                passReqToCallback : true
            },
            function (req, username, password, done) {
                for (var i = 0; i < users.length; i++) {
                    if (username === users[i].username) {
                        if (password === users[i].password){
                            return done(null, users[i]);
                        }
                        else {
                            console.log('Invalid password for user ' + username);
                            return done(null, false);
                        }
                    }
                }
                console.log("User not found: " + username);
                return done(null, false);
            }
        ));
};


