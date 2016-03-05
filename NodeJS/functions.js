// vendor library
var passport = require('passport');
var bcrypt = require('bcrypt-nodejs');

// custom library
// model
var Model = require('./database/model');


// index
var index = function(req, res, next) {
    if(!req.isAuthenticated()) {
        res.redirect('index',302);
    } else {

        var user = req.username;

        if(user !== undefined) {
            user = user.toJSON();
        }
        res.render('index', {user: user});
    }
};

// sign in
// Get
var signIn = function(req, res, next) {
    if(req.isAuthenticated()) res.redirect('/home');
    res.render('index');
};

// sign in
// POST
var signInPost = function(req, res, next) {
    passport.authenticate('local', { successRedirect: '/home',
        failureRedirect: '/index'}, function(err, user, info) {
        if(err) {
            return res.render('index', {title: 'Sign In', errorMessage: err.message});
        }

        if(!user) {
            return res.render('index', {title: 'Sign In', errorMessage: info.message});
        }
        return req.logIn(user, function(err) {
            if(err) {
                return res.render('index', {title: 'Sign In', errorMessage: err.message});
            } else {
                return res.redirect('/home');
            }
        });
    })(req, res, next);
};


// sign up
// GET
var signUp = function(req, res, next) {
    if(req.isAuthenticated()) {
        res.redirect('/');
    } else {
        res.render('signup', {title: 'Sign Up'});
    }
};

// sign up
// POST
var signUpPost = function(req, res, next) {
    var user = req.body;
    var usernamePromise = null;
    usernamePromise = new Model.User({username: user.username}).fetch();

    return usernamePromise.then(function(model) {
        if(model) {
            res.render('signup', {title: 'signup', errorMessage: 'username already exists'});
        } else {
            //****************************************************//
            // MORE VALIDATION GOES HERE(E.G. PASSWORD VALIDATION)
            //****************************************************//
            var password = user.password;
            var hash = bcrypt.hashSync(password);

            var signUpUser = new Model.User({username: user.username, password: hash});

            signUpUser.save().then(function(model) {
                // sign in the newly registered user
                signInPost(req, res, next);
            });
        }
    });
};

// sign out
var signOut = function(req, res, next) {
    if(!req.isAuthenticated()) {
      //todo route to 404 page
    } else {
        req.logout();
        res.redirect('/signin');
    }
};

// export functions
/**************************************/
// index
module.exports.index = index;

// sigin in
// GET
module.exports.signIn = signIn;
// POST
module.exports.signInPost = signInPost;

// sign up
// GET
module.exports.signUp = signUp;
// POST
module.exports.signUpPost = signUpPost;

// sign out
module.exports.signOut = signOut;

