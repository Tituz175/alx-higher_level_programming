#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const bodyData = JSON.parse(body);
    const resObj = {};
    bodyData.forEach(data => {
      if (data.completed) {
        resObj[data.userId] = resObj[data.userId] ? resObj[data.userId] + 1 : 1;
      }
    });
    console.log(resObj);
  }
});
