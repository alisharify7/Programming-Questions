let numbers = [10,9,8,7,6,5,4,3,2,1];
for (let i = 0; i < numbers.length; i++)
{   
    for (let j = 0; j < (numbers.length); j++)
    {
        let temp = numbers[j];
        if (temp > numbers[j+1])
        {
            let temp1 = numbers[j+1];
            numbers[j+1] = temp;
            numbers[j] = temp1; 
            console.log(numbers);
        }
        else
        {
            continue;
        }
        
    }
 }