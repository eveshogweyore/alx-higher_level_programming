#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];

  const lastIndex = list.length - 1;

  for (let i = lastIndex; i >= 0; i--) {
    newList.push(list[i]);
  }

  return newList;
};
