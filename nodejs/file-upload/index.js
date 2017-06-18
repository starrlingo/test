var express = require('express');
var multer = require('multer'),
    bodyParser = require('body-parser'),
    path = require('path');

var app = new express();
app.use(bodyParser.json());

app.get('/', function(req, res){
  res.render('index');
});

var upload = multer({ dest: './uploads/' })

app.post('/singleUpload', upload.single('singleUpload'), function(req,res){
    console.log(req.body); //form fields
    /* example output:
    { title: 'abc' }
     */
    console.log(req.file); //form files
    /* example output:
            { fieldname: 'upl',
              originalname: 'grumpy.png',
              encoding: '7bit',
              mimetype: 'image/png',
              destination: './uploads/',
              filename: '436ec561793aa4dc475a88e84776b1b9',
              path: 'uploads/436ec561793aa4dc475a88e84776b1b9',
              size: 277056 }
     */
    res.status(204).end();
});

app.post('/multiUpload', upload.array('multiUpload', 12), function (req, res, next) {
  // req.files is array of `photos` files
  // req.body will contain the text fields, if there were any
    console.log(req.files); //form files
    res.status(204).end();
});

var port = 3000;
app.listen( port, function(){ console.log('listening on port '+port); } );