#!/usr/bin/node

const number_list = process.argv.slice(2, -1);

if (number_list.length > 1) {
  max_number = number_list.reduce((a, b) => (a > b ? a : b));
  number_list.splice(number_list.indexOf(max_number), 1);
  console.log(number_list.reduce((a, b) => (a > b ? a : b)));
} else {
  console.log(0);
}
