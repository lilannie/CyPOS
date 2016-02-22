var gulp = require('gulp');
var uglify = require('gulp-uglify');
var browserify = require('browserify');

var path = {
    OUT            : 'bundle.js',
    DEST_BUILD     : 'js/',
    ENTRY_POINT    : './components/main.js'
};

gulp.task('build', function() {
    browserify({
        entries   : [path.ENTRY_POINT],
        transform : [reactify]
    })
        .bundle()
        .pipe(source(path.OUT))
        .pipe(streamify(uglify(path.OUT)))
        .pipe(gulp.dest(path.DEST_BUILD));
});

gulp.task('default', ['build']);