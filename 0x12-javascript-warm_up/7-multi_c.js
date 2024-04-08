#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] === undefined) {
  console.log('Missing number of occurrences');
}

const size = parseInt(argv[2]);

for (let i = 0; i < size; i++) {
  console.log('C is fun');
}
