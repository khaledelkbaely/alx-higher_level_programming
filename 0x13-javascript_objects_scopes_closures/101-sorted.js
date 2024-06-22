#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
Object.entries(dict).forEach(([key, value]) => {
  if (newDict[value]) { newDict[value] = newDict[value].concat([key]); } else { newDict[value] = [].concat([key]); }
});
console.log(newDict);
