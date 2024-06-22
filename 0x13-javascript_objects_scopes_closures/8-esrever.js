#!/usr/bin/node
exports.esrever = function esrever (list) {
  if (list.length === 0) {
    return [];
  }
  const rest = esrever(list.slice(1));
  rest.push(list[0]);
  return rest;
};
