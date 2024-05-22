#!/usr/bin/node

const process = require('process');
const fs = require('node:fs');

const file = process.argv[2];
const content = process.argv[3];

fs.writeFile(file, content, err => {
  if (err) {
    console.error(err);
  }
});
