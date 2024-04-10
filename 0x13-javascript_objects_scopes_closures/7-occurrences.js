#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (const listValue of list) {
    if (listValue === searchElement) {
      count += 1;
    }
  }

  return count;
};
