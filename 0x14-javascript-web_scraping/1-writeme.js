#!/usr/bin/node
// a script that writes a string to a file
let fs = require('fs');
let process = require('process');
let args = process.argv;
fs.writeFile(args[2], args[3], 'utf8', function(err){
	if (err) throw err;
});
