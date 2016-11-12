var gulp = require('gulp');
var less = require('gulp-less');
var browserSync = require('browser-sync').create();
var header = require('gulp-header');
var cleanCSS = require('gulp-clean-css');
var rename = require("gulp-rename");
var uglify = require('gulp-uglify');

gulp.task('copy', function() {
  gulp.src(['node_modules/d3/build/d3.js', 'node_modules/d3/build/d3.min.js'])
    .pipe(gulp.dest('public/vendor/d3/build'));

  gulp.src(['node_modules/d3-*/build/d3-*.js', 'node_modules/d3-*/build/d3-*.min.js'])
    .pipe(gulp.dest('public/vendor/'));
});

gulp.task('default', ['copy']);
