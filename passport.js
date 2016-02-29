var LocalStrategy = require('passport-local').Strategy;

module.exports = function (passport, repository) {
    passport.serializeUser(function (user, done) {
        done(null, user.id);
    });

    passport.deserializeUser(function (id, done) {
        repository.getUserById(id)
            .then(function (user) {
                done(null, user);
            });
    });

    passport.use(
        'login',
        new LocalStrategy({
                usernameField     : 'username',
                passwordField     : 'password',
                passReqToCallback : true
            },
            function (req, username, password, done) {
                repository.getUserByUsername(username)
                    .then(function (user) {
                        if (user === null) {
                            console.log("User not found: " + username);
                            return done(null, false);
                        } else {
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
        )
    )
};