#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const chP = c || 'X';
    let ln = '';
    for (let i = 0; i < this.width; i++) { ln += chP; }
    for (let i = 0; i < this.height; i++) { console.log(ln); }
  }
}
module.exports = Square;
