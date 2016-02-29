var path    =   __dirname + '/public/views/';

function authenticated(request, response, next) {
    if (request.isAuthenticated()) return next();
    else response.redirect('/index');
}
var loggedInUsers = [];
function isLoggedIn (username) {
    for (var user in loggedInUsers) {
        if (user === username) return true;
    }
    return false;
}
module.exports = function (app, passport, io, repository, express) {

    app.get('/', function (request, response) {
        response.sendFile(path + '/index.html');
    });
    app.post(
        '/',
        passport.authenticate('login', {
            successRedirect : '/home',
            failureRedirect : '/'
        }),
        function (request, response) {
            console.log("User logged in successfully.");
        }
    );
    app.get("/home",function(req,res){
        res.sendFile(path + "home.html");
    });
    app.get("/classes",function(req,res){
        res.sendFile(path + "classes.html");
    });
    app.get("/help",function(req,res){
        res.sendFile(path + "help.html");
    });
    app.get("/history",function(req,res){
        res.sendFile(path + "history.html");
    });
    app.get("/home",function(req,res){
        res.sendFile(path + "home.html");
    });
    app.get("/manage",function(req,res){
        res.sendFile(path + "manage.html");
    });
    app.get("/myaccount",function(req,res){
        res.sendFile(path + "myaccount.html");
    });
    app.get("/new",function(req,res){
        res.sendFile(path + "new.html");
    });
    app.get("/view",function(req,res){
        res.sendFile(path + "view.html");
    });

    app.get('/logout', function (request, response) {
        loggedInUsers = loggedInUsers.filter(function (user) {
            return user !== request.user.get('username');
        });
        io.emit('out', {username: request.user.get('username')});
        request.logout();
        response.redirect('/');
    });

    io.on('connection', function () {
        console.log('Connected to IO server');
    });
}



