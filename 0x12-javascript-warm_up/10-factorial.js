#!/usr/bin/node

const number = process.argv[2];

let result = 1;

for (let i = 1; i <= number; i++) {
  result *= i;
}
console.log(result);
