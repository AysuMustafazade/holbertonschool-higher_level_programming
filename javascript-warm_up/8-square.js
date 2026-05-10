#!/usr/bin/node
const myVar = parseInt(process.argv[2], 10);
if (Number.isInteger(myVar)) {
  for (let i = 0; i < myVar; i++) {
      for (let j = 0; j < myVar; j++) {
          console.log('X');
        }
    }
} else {
  console.log('Missing size');
}
