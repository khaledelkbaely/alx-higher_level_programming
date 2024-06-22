#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const c = 'X';
    let ln = '';
    for (let i = 0; i < this.width; i++) { ln += c; }
    for (let i = 0; i < this.height; i++) { console.log(ln); }
  }
}
module.exports = Rectangle;
