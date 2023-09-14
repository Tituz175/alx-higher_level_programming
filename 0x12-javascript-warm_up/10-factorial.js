#!/usr/bin/node

const number = process.argv[2];

function factorial (n) {
  let result = 1;

  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  console.log(result);
}
factorial(number);
