#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] === undefined || Number.isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
}

const size = parseInt(argv[2]);

for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    process.stdout.write('X');
  }
  console.log('');
}
