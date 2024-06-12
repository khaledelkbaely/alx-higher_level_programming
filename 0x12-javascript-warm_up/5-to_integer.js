#!/usr/bin/node
let n = parseInt(process.argv[2])
console.log(Number.isInteger(parseFloat(process.argv[2])) ? 'My number: '.concat(n) : 'Not a number');
