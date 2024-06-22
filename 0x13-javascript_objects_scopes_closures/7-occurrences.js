#!/usr/bin/node
exports.nbOccurences = function nbOccurences (list, searchElement) {
  if (list.length === 0) {
    return 0;
  }
  const e = list[0];
  if (e === searchElement) { return 1 + nbOccurences(list.slice(1), searchElement); } else { return nbOccurences(list.slice(1), searchElement); }
};
