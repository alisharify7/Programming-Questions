#include <stdio.h>
#include <string.h>

int main(void)
{


    // reverse a string
    char name [40];
    printf("Enter a string: ");
    scanf("%s",name);

    printf ("After the reverse of a string: %s ", strrev(name));  
    return 0;

}   