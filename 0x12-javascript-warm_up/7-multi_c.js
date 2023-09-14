#!/usr/bin/node

const total = process.argv[2];

if (!total) {
  console.log('Missing number of occurances');
} else {
  for (let i = 0; i < total; i++) {
    console.log('C is fun');
  }
}
