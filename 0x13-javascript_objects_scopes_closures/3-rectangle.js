#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0) {
      // pass
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let j = 0; j < this.width; j++) {
        output += 'X';
      }
      console.log(output);
    }
  }
}

module.exports = Rectangle;
