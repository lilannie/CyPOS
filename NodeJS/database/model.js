module.exports = function (bookshelf) {
    var User = bookshelf.Model.extend({
        tableName : 'tblUsers'
    });

    var Course = bookshelf.Model.extend({
        tableName: 'tblCourses'
    });

    return {
        User    : User,
        Course : Course
    };
};