#!/usr/bin/node

const argc = process.argv.length;
const argv = process.argv;

if (argc === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
