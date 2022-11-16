#!/usr/bin/node
// A script to print the title of a star wars movie
let process = require('process')
let args = process.argv.slice(2)
let request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + args[0], function(err, res, body){
	//if (err) throw err;
	//res.stringify();
	console.log(JSON.parse(body).title)
});
