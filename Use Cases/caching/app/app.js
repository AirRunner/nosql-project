const express = require('express');
const axios = require('axios');
const redis = require('redis');

const listenPort = 3160;
const app = express();

const redisPort = 6379;
const redisClient = redis.createClient(redisPort);

redisClient.on('error', (err) => {
    console.log("Error: " + err);
});


app.get('/countries', (req, res) => {
    const query = (req.query.query).trim();
    const searchUrl = `https://restcountries.eu/rest/v2/lang/${query}`;
    
    return redisClient.get(`countries:${query}`, (err, result) => {
        if (result) {
            const resultJSON = JSON.parse(result);
            return res.status(200).json(resultJSON);
        }
        else {
            return axios.get(searchUrl)
            .then(response => {
                const responseJSON = response.data;
                redisClient.setex(`countries:${query}`, 3600, JSON.stringify({ source: 'Redis Cache', content: { ...responseJSON }, }));
                return res.status(200).json({ source: 'Countries API', content: { ...responseJSON }, });
            })
            .catch(err => {
                return res.json(err);
            });
        }
    });
});

app.listen(listenPort, () => {
    console.log('Server listening on port: ', listenPort);
});
