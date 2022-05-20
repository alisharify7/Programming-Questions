#include <stdio.h>
#include <stdbool.h>

// this function decides input number is 
// even or odd
bool even_odd(int number)
{
    if (number % 2 == 0)
    {
        return true;
    }
    return false;
}


int main(void)
{
    // get input from user
    int user;
    printf("Enter a number: ");
    scanf("%d", &user);

    while (true)
    {
        // if number is one break
        if (user == 1)
        {
            printf("Number is %i \n", user);
            break;
        }

        // if number is even
        // divided by 2
        if (even_odd(user) == true)
        {
            printf("Number is %i \n",user);
            user = user / 2;
            continue;
        }
        
        // if number is odd
        // multiplied by 3 and add one 
        if (even_odd(user) == false)
        {
            printf("Number is %i \n",user);
            user = (user * 3) + 1;
            continue;   
        }
    }

}