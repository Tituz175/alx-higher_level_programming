#!/usr/bin/node

const total = process.argv[2];

if (!parseInt(total)) {
  console.log('Missing size');
} else {
  if (total > 0) {
    let response = '';
    for (let i = 0; i < total; i++) {
      for (let j = 0; j < total; j++) {
        response += 'X';
      }
      if (i !== total - 1) {
        response += '\n';
      }
    }
    console.log(response);
  }
}
