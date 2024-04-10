#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

fs.readFile(argv[2], 'utf8', (err, fileContent) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(argv[4], fileContent, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return -1;
    }
  });
});

fs.readFile(argv[3], 'utf8', (err, fileContent) => {
  if (err) {
    console.error(err);
    return -1;
  }
  fs.appendFile(argv[4], fileContent, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return -1;
    }
  });
});
