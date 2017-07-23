var fs = require('fs');
var execSync = require('child_process').execSync;
var Q = require('q');
var mv = require('mv');
var rimraf = require('rimraf');
var tempFolder = './temp';
var rmDir = Q.denodeify(rimraf);
var moveDir = Q.denodeify(mv);

console.log('sub proccess initiated');

Q.resolve(true)
.then(resp => {
    var task = [];
    task.push(moveDir('./source/source0', tempFolder + '/source0', {mkdirp: true}));
    task.push(moveDir('./source/source1', tempFolder + '/source1', {mkdirp: true}));
    return Q.all(task);
})
.then(resp => {
    console.log('move source0 & source1 to temp');
    console.log('start to move new-source to source');
    execSync("sleep 10"); // do some time consuming job
    var task = [];
    task.push(moveDir('./new-source', './source', {clobber: false}));
    return Q.all(task);
})
.then(resp => {
    console.log('end move new source to source');
    return rmDir(tempFolder);
})
.then(resp => {
    console.log('remove temp');
    console.log('sub process ended');
})
.catch(err => {
    console.error('sub process error:', err.message);
})