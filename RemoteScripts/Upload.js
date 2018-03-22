'use strict'

var fs = require('fs');
var gulp = require('gulp');
var GulpSSH = require('gulp-ssh');

console.log('upload');

var config = {
  host: '10.3.23.195',
  port: 22,
  username: 'pi',
  password: 'setuphku'
}

var gulpSSH = new GulpSSH({
  ignoreErrors: false,
  sshConfig: config
})

gulp.task('sftp-write', function () {
  return gulp.src('Run.js')
    .pipe(gulpSSH.sftp('write', '/home/pi/test/run.js'))
})

console.log('done');