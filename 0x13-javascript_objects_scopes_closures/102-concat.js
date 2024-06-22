#!/usr/bin/node
const fs = require('fs');

const f1Data = fs.readFileSync(process.argv[2], 'utf8');
const f2Data = fs.readFileSync(process.argv[3], 'utf8');

fs.appendFileSync(process.argv[4], f1Data + f2Data, 'utf8');
