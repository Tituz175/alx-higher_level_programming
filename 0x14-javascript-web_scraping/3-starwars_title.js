#!/usr/bin/node
// a script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const episodeNumber = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}`;

// request.get(url).on('response', function (response) {
//   console.log(response.body);
// });

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
