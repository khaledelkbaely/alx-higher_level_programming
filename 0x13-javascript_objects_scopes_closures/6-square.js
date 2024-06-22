#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    const chP = c || 'X';
    let ln = '';
    for (let i = 0; i < this.width; i++) { ln += chP; }
    for (let i = 0; i < this.height; i++) { console.log(ln); }
  }
}
module.exports = Square;
