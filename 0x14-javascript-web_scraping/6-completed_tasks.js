#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], { json: true }, (error, response, todos) => {
  if (error) {
    console.error(error);
  }

  const records = {};
  for (const todo of todos) {
    if (records[todo.userId] === undefined) {
      records[todo.userId] = 0;
    }

    if (todo.completed === true) {
      records[todo.userId] += 1;
    }
  }

  console.log(records);
});
