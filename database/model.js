module.exports = function (bookshelf) {
    var User = bookshelf.Model.extend({
        tableName : 'tblUsers',
        idAttribute: 'userID'
    });

    return {
        User    : User
    };
};