module.exports = function (models, bookshelf) {
    var Users = bookshelf.Collection.extend({
        model: models.User
    });
    
    var Courses = bookshelf.Collection.extend({
        model: models.Courses
    });

    return {
        Users: Users,
        Courses: Courses
    };
};
