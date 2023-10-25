#!/usr/bin/node
// a script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const id = 18

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    data.results.forEach(element => {
      element.characters.forEach(link => {
        if (link.includes(id)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
