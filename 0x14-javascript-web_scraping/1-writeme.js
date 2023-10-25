#!/usr/bin/node
// a script that writes a string to a given file

const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];
fs.writeFile(file, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
