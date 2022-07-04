const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
  
readline.question('Enter a Number:', number => {
    for(let i = 1; i <= number;i++)
    {
      for (let j = 0; j<i; j++){
        process.stdout.write("*");
      }
      console.log();
    }
  readline.close();
});
