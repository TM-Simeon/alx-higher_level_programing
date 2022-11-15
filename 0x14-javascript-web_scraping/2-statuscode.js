#!/usr/bin/node
// write a script that display the status code of a get request
let request = require('request');
let process = require('process');
let args = process.argv;
request
	.get(args[2],)
	.on('response', function(response){
		console.log("code: %s", response.statusCode)
	});
