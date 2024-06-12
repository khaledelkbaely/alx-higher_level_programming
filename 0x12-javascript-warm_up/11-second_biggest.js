#!/usr/bin/node
const args = process.argv.slice(2).sort();
console.log(args.length < 2 ? 0 : args[args.length - 2]);
