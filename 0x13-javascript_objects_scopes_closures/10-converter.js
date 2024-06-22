#!/usr/bin/node
exports.converter = function converter (base) {
  return numberBase10 => numberBase10.toString(base);
};
