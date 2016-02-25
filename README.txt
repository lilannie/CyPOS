Jens Petersen
George Zachariades
Rockie Brooks
Annie Steenson

Developer Notes:
-------------------------------------------
Rocky-> Your stuff is ready to insert into new.html


Uses:
-------------------------------------------
Install dependencies on local: "npm install"
Run server on localhost: "npm start"
Access website at: "localhost:8080"


HTTP Routing:
-------------------------------------------
localhost:8080/ or localhost:8080/index.html   --> login page
localhost:8080/home --> home page setup with no login info


Directory Structure:
-------------------------------------------
database: DB scripts
files: extra files for testing, reference, etc.
lib: external library files
public: public html, css, js files that are seen by the user
util: utility scripts
root directory: scripts ran on the server


Node Modules Used:
-------------------------------------------
Express.js: Bundled minddlewares for configuring our application.
Bootstrap.js: <descrip>
Bcrypt-nodejs: Encrypts password before we store it
Ejs: javascript templating engine, allows us to execute some inline codes within our page
Passportjs: Authentication middleware designed for users
Passport-local: Because were using our own database for authentication
Bookshelfjs: ORM, use lists of functions to query
MySQL: Work with MySQL database


