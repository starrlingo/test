var fs = require('fs');
var spawn = require('child_process').spawn;
var Q = require('q');
var mv = require('mv');

var moveDir = Q.denodeify(mv);
var access = Q.denodeify(fs.access);

var subTask = spawn('node', ['./subProcess.js']);

subTask.stdout.on('data', function (data) {
  console.log('stdout: ' + data);
});

subTask.stderr.on('data', function (data) {
  console.log('stderr: ' + data);
});

subTask.on('close', function(code) {
  console.log('end code: ' + code);
});

setTimeout(function() {
    process.kill(subTask.pid);

    if (fs.existsSync('./temp')) {
        mv('./temp', './source', {clobber: false}, function(err) {
            if (err) {
                console.error('Can not mv temp to source folder:', err.message);
            }
            console.log('Recover source folder from temp');
        });
    } else {
        console.log('./temp not found');
    }
}, 2000);