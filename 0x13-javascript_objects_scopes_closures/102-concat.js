#!/usr/bin/node

const fs = require('fs');

const fileOne = process.argv[2];
const fileTwo = process.argv[3];

const dataOne = fs.readFileSync(fileOne, 'utf8');
const dataTwo = fs.readFileSync(fileTwo, 'utf8');

fs.writeFileSync(process.argv[4], dataOne + dataTwo);
