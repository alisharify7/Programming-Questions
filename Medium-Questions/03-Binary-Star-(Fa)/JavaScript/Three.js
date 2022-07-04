function dec2bin(dec) {
    return (dec >>> 0).toString(2);
}

function find1(number){
    let counter = 0;
    for(let each of number)
    {
        if (each == "1")
        {
            counter++;
        }
    }
    return counter;
}

function Start_printer(number)
{
    let answer = "";
    for (let i = 1; i <= number; i++)
    {
        for (let  j = 0; j < i; j++){
            answer += " # ";
        }
        answer += "<br/>";
    }
    return answer;
}

let number = prompt("Number: ");
let BinNumber = dec2bin(number);
let oneNumber = find1(BinNumber);
let answer = Start_printer(oneNumber);

document.getElementById('answer').innerHTML = answer;