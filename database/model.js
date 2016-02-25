var DB = require('./db').DB;

var User = DB.Model.extend({
    tableName: 'tblUsers',
    idAttribute: 'userID',
});

module.exports = {
    User: User
};