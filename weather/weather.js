const request = require('request');
//39.2590567,-76.8951551 - Ellicott City MD
//API KEY: 7559731c585814f3c2efa58a679f2aad
let getWeather = (lat, lng, callback) => {
    request({
        url: `https://api.darksky.net/forecast/7559731c585814f3c2efa58a679f2aad/${lat},${lng}`
    }, (error, response, body) => {
        var body = JSON.parse(body);
        if (!error && response.statusCode === 200) {
            // console.log(body.currently.ter,)
            var ret = {
                temperature: Math.round(body.currently.temperature), //Units are not provided
                feelsLike: body.currently.apparentTemperature, //Units will have to be defined in console.log
                summary: body.currently.summary, //Only numbers are given
                windSpeed: body.currently.windSpeed
            };
            callback(undefined, ret);
        } else {
            // console.log("Unable to get weather");
            callback("Unable to get weather");
        }
    })
};
module.exports.getWeather = getWeather;