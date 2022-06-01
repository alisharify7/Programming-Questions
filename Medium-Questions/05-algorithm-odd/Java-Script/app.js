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


let user = ParseInt(prompt("Enter a Number: "));
console.log(user);


while(true)
{
    if (user < 0)
    {
        break;
    }

    if (user == 1)
    {
        console.log("User input is One");
        break;
    }

    else if(even(user))
    {
        user = user / 2;
        console.log(user);
    }

    else
    {
        user = (user * 3) + 1;
        console.log(user);
    }
}