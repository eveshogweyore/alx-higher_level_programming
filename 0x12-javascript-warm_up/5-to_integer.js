#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] === undefined || Number.isNaN(parseInt(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(argv[2])}`);
}
