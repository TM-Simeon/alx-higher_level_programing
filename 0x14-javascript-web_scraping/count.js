#!/usr/bin/node
// increament a value
let value = 0;
function myvalue(){
	for (let i = 4; i < 10; i++){
		value += 1;
	}
	return value;
}
console.log(myvalue())
