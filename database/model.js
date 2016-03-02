module.exports = function (bookshelf) {
    var User = bookshelf.Model.extend({
        tableName : 'tblUsers',
        idAttribute: 'userID'
    });

    var Course = bookshelf.Model.extend({
        tableName: 'tblCourses',
        idAttribute: 'courseID'
    });

    return {
        User    : User,
        Course : Course
    };
};