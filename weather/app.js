const geocode = require('./geocode');
const weather = require('./weather');
// const input = require('readline-sync')
const express = require('express');
// const hbs = require('hbs');
console.log("Starting App");
// console.log("Welcome to a weather app");
var app = express();
// var address = input.question("Enter a location: ");
// app.set('view engine','hbs');
app.use(express.static(__dirname + '/public'));
app.get('/', function (req, res) {
    res.sendfile('weather/index.html');
});
app.get('/weather/:address',(req,res) => {
    var address = req.params.address;
    geocode.geocodeAddress(address, (errorM, results) => {
        if(errorM){
            console.log(errorM);
            console.log("There was an error");
        }else{
            // console.log(results)
            weather.getWeather(results.latitude,results.longitude,(errorW,data) => {
                var rdata = {
                    latitude: results.latitude,
                    longitude: results.longitude,
                    address: results.address,
                    temp: data.temperature,
                    feelsLike: data.feelsLike,
                    windSpeed: data.windSpeed,
                    summary: data.summary
                };
                console.log(rdata.feelsLike)
                res.send(JSON.stringify(rdata,undefined,2))
            });
        }
    })
});
app.listen(7500)