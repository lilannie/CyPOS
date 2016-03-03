module.exports = function (Models, Collections) {
    // USERS \\
    function getAllUsers () {
        return Collections.Users.forge().fetch();
    }

    function getUserById (id) {
        return Models.User.forge({userId : id}).fetch();
    }

    function getUserByUsername (username) {
        return Models.User.forge({username : username}).fetch({require : true});
    }

    function createUser (username, password, email, name, lastname) {
        return Models.User.forge({
                username : username,
                password : password,
                email: email,
                name: name,
                lastname: lastname,
            })
            .save();
    }

    return {
        getAllUsers         : getAllUsers,
        getUserById         : getUserById,
        getUserByUsername   : getUserByUsername,
        createUser          : createUser
    };
};