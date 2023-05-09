let date1 = new Date(year=2023,month=5,day=8, hour=20);
let date2 = new Date(year=2023,month=5,day=8, hour=18);
console.log(date1);
console.log(date2);

// result of this statement is Millisecond
let ans = Math.abs(date2 - date1);
// convert to second
ans /= 1000;
// convert to minute
ans /= 60;
// convert to Hour
ans /= 60;

console.log(`The Delta Between To date is ${ans} Hour`);
