const readLine = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readLine.question("Inter the number: ", validation);

function validation(number) {
  //String to Number
  const num = Number(number);

  let state = "not valid - Odd Number";

  if (num >= 100 || num < 1) {
    state = "Invalid Number - Number must Between 1 to 100";
  } else if (num % 2 === 0) {
    state = "valid - Even Number";
  }

  readLine.close();
  console.log(state);
  return state;
}

module.exports = validation;
