'use strict'

var gulp = require('gulp');
var GulpSSH = require('gulp-ssh');

var parameterIndex = process.argv.indexOf("--ip");
var ip = (parameterIndex+1 < process.argv.length) ? process.argv[parameterIndex+1] : '10.3.23.92';

var config = {
  host: ip,
  port: 22,
  username: 'pi',
  password: 'setuphku'
};

var gulpSSH = new GulpSSH({
  ignoreErrors: false,
  sshConfig: config
});

gulp.task('uploadProject', function () {
  return gulp
    .src(['../robot/**', '!**/.idea/**'])
    .pipe(gulpSSH.dest('/home/pi/machina/'))
});

gulp.task('uploadCode', function () {
  return gulp
    .src(['../robot/venv/Scripts/**'])
    .pipe(gulpSSH.dest('/home/pi/machina/venv/Scripts/'))
});

gulp.task('run', ['uploadCode'], function () {
  const logName = (new Date()).getTime() + '.txt';
  return gulpSSH
    .exec(['python /home/pi/machina/venv/Scripts/main.py'], {filePath: logName})
    .pipe(gulp.dest('logs/')).on('data', function(data) {
      console.log('STDOUT: ' + data);
    });
});

gulp.task('upload', [ 'uploadProject']);
gulp.task('default', [ 'uploadCode', 'run']);
