#include <stdio.h>

int main(void)
{   

    int user;
    // get input from user
    printf("Enter a Number: ");
    scanf("%i", &user);

    // check for number between 1 to 100
    if (user > 0 && user < 100)
    {
        // check for Number is even or odd
        if (user % 2 == 0)
        {
            printf("it's Even Number :) ");
            return 0;
        }
        else
        {
            printf("Its odd Number :) ");
            return 0;
        }
    }
    // if number is out of Range
    else
    {
        printf("Invalid Number - Number must Between 1 to 100");
        return 0;
    }

}