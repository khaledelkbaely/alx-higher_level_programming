#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (Number.isNaN(n)) process.exit();
for (let i = 0; i < n; i++) {
  console.log('C is fun');
}
