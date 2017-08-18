var fs = require('fs');
var Client = require('ssh2').Client;

var conn = new Client();
var privateKey = fs.readFileSync('/path/to/id_rsa');
// var privateKey = `
// -----BEGIN RSA PRIVATE KEY-----
// key here
// -----END RSA PRIVATE KEY-----
// `

conn.on('ready', function() {
  console.log('Client :: ready');
  conn.exec('uptime', function(err, stream) {
    if (err) throw err;
    stream.on('close', function(code, signal) {
      console.log('Stream :: close :: code: ' + code + ', signal: ' + signal);
      conn.end();
    }).on('data', function(data) {
      console.log('STDOUT: ' + data);
    }).stderr.on('data', function(data) {
      console.log('STDERR: ' + data);
    });
  });
}).connect({
  host: '172.17.28.130',
  port: 22,
  username: 'admin',
  privateKey: privateKey
});
