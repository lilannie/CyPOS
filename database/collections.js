module.exports = function (models, bookshelf) {
    var Users = bookshelf.Collection.extend({
        model: models.User
    });



    return {
        Users: Users
    };
};