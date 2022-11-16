#!/usr/bin/node
// find the number of movies he acted
let request = require('request')
let count = 0;
url = 'https://swapi-api.hbtn.io/api/people/18/' 
//request('https://swapi-api.hbtn.io/api/films', function(err, response, body){
request(process.argv[2], function(err, response, body){ 
	JSON.parse(body).results.forEach(ele => {
		(ele).characters.forEach(character => {
	if ( character === url ) { count += 1; }
	//console.log(character)
	})
		//console.log(count);
	})
	console.log(count);
});
