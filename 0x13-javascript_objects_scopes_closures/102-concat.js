#!/usr/bin/node
const list = require('./100-data').list;

const mapped = list.map((n, idx) => n * idx);
console.log(list);
console.log(mapped);
