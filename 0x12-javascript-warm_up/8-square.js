#!/usr/bin/node
const n = parseInt(process.argv[2]);
const ch = 'X';
if (Number.isNaN(n)) {
  console.log('Missing size');
  process.exit();
}
for (let i = 0; i < n; i++) {
  let c = ch;
  for (let i = 1; i < n; i++) {
    c += ch;
  }
  console.log(c);
}
