const express = require('express');
const request = require('request');
const fs = require('fs');

var bodyParser = require('body-parser');

var initError = "Initial error.";
var initPortTelecom = 80;
var initInfernet = "http://localhost/";
var initPlot = initInfernet+initPortTelecom;
var prErr = "[PL:MX] ";
var prInf = "[PL:MQ] ";
var prInt = "[PL:MXQ] ";
var prNor = "[PL] ";

app = express();
const port = 4040;

function isJsonString(str) {
	try {
		JSON.parse(str);
	} catch (e) {
		return false;
	}
	return true;
}

function prox(json) {
	const init = null;
}

const errJsonInv = {"error": "Invalid type of string"};
// Use addon for express
app.use(bodyParser.json());

app.post('/api', function(request, response) {
	console.log(request.body);
	var valid = isJsonString(request.body);
	if(valid === true) {
		console.log("We did it")
	}
	res.send(JSON.parse(errJsonInv))
})

app.listen(port, function(){
	console.log(prNor+"Initial response Object:0x0")
	console.log(prNor+"Listening on port "+port)
});
