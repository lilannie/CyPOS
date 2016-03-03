// load all the things we need
var LocalStrategy   = require('passport-local').Strategy;

var users = [
    {
        username: 'Annie',
        password: 'foo'
    }
];

// expose this function to our app using module.exports
module.exports = function(passport, repository) {

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
                console.log("here");

                repository.getUserByUsername(username)
                    .then(function (user) {
                        if (user === null) {
                            console.log("User not found: " + username);
                            return done(null, false);
                        } else {

                            console.log("username: "+username);
                            console.log("password: "+password);
                            if (user.get('password') === password) {
                                return done(null, user);
                            } else {
                                console.log('Invalid password for user ' + username);
                                return done(null, false);
                            }
                        }
                    })
                    .catch(function (err) {
                        console.log(err.message);
                        return done(null, false);
                    });
            }
        ));
};


