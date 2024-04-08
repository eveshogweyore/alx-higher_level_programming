#!/usr/bin/node

const { argv } = require('node:process');

const size = parseInt(argv[2]);

function factorial (s) {
  if (Number.isNaN(s)) {
    return 1;
  }

  if (s === 0) {
    return 1;
  }

  return s * factorial(s - 1);
}

console.log(factorial(size));
