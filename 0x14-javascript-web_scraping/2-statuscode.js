#!/usr/bin/node

const process = require('process');
const request = require('request');

request
  .get(process.argv[2])
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });
