// this function Specifies is a number even or odd
function even(number)
{
    if (number % 2 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

let answer = document.getElementById("answer");
let user = prompt("Enter a Number: ");
console.log(user);


while(true)
{
    if (user < 0)
    {
        answer.innerHTML = "Number is one DOne";
        break;
    }
    
    if (user == 1)
    {
        answer.innerHTML += "<br/>" + "User input is One";
        console.log("User input is One");
        break;
    }
    
    else if(even(user))
    {
        user = user / 2;
        answer.innerHTML += `<br/>  ${user}` ;
        console.log(user);
    }
    
    else
    {
        user = (user * 3) + 1;
        answer.innerHTML += `<br/>  ${user}` ;
        console.log(user);
    }
}