#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] === undefined || argv.length === 3) {
  console.log(0);
} else {
  let max;
  let smax;

  if (parseInt(argv[2]) > parseInt(argv[3])) {
    max = parseInt(argv[2]); smax = parseInt(argv[3]);
  } else {
    max = parseInt(argv[3]); smax = parseInt(argv[2]);
  }

  for (let i = 3; i < argv.length; i++) {
    if (max < parseInt(argv[i])) {
      smax = max;
      max = parseInt(argv[i]);
    }
  }

  console.log(smax);
}
