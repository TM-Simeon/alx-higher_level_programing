#!/usr/bin/node
// get the content of a web page and store it
let fs = require('fs')
let request = require('request')
request(process.argv[2], function(err, response, body){
	fs.writeFile(process.argv[3], body,'utf8', function(err){
		if (err) throw err;
	});
});
