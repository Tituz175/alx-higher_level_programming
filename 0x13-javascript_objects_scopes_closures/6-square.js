#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (side) {
    super(side, side);
  }

  charPrint (char = 'X') {
    if (this.width > 0 && this.height > 0) {
      let response = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          response += char;
        }
        if (i !== this.height - 1) {
          response += '\n';
        }
      }
      console.log(response);
    }
  }
}

module.exports = Square;
