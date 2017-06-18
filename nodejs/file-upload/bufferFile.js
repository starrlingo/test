var fs = require('fs');

// read file as base64 encoded buffer and revert back to file
fs.readFile('./sample/test2.zip', function (err, data ) {
    var base64Data = data.toString('base64');
    // try to decode
    var originaldata = new Buffer(base64Data, 'base64');
    // save as file
    fs.writeFile('./data/data2.zip', originaldata, 'binary', function(err){
        if (err) throw err
        console.log('File saved.')
    });
});

// write buffer to file
var bufferData = Buffer.from("test123");
console.log(bufferData);
console.log(bufferData.toString('base64'));
fs.writeFile('./data/data1.txt', bufferData, 'binary', function(err){
    if (err) throw err
    console.log('File saved.')
});