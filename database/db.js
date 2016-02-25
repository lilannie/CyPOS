var Bookshelf = require('bookshelf');

var config = {
    host: 'mysql.cs.iastate.edu',  // your host
    user: 'dbu309grp17', // your database user
    password: 'AugtUmP22JP', // your database password
    database: 'db309grp17',
    charset: 'UTF8_GENERAL_CI'
};

var DB = Bookshelf.initialize({
    client: 'mysql',
    connection: config
});

module.exports.DB = DB;