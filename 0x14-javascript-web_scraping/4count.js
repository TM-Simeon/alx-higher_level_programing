#!/usr/bin/node
// a script that prints the number of movies given ID
const process = require('process')
const request = require('request')
let args = process.argv.slice(2);
let url = 'https://swapi-api.hbtn.io/api/films/'
let character = 'https://swapi-api.hbtn.io/api/films/18/'
let count = 0

function inList(psString, psList){
	var laList = psList.split(',');
	var i = laList.length;
	while (i--) {
		if (laList[i] === psString)
			return true;
	}
	return false;
}
	
request(url, function(err, response, body){
	if (err) throw err;
	JSON.parse(body).results.forEach(result => {
		if (inList(character, result.characters){
			console.log('yes');
		}
		//console.log(result);
	});
console.log(count)
});
