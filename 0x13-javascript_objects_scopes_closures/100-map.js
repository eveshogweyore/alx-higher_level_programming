#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((listValue, idx, list) => {
  return listValue * idx;
});

console.log(list);
console.log(newList);
