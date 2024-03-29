#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      let response = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          response += 'X';
        }
        if (i !== this.height - 1) {
          response += '\n';
        }
      }
      console.log(response);
    }
  }
}

module.exports = Rectangle;
