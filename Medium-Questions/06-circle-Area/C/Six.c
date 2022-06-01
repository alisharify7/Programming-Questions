#include <stdio.h>

float pi = 3.14159265359;

int main(void)
{
    // get input form user
    int r;
    printf("Enter radius: ");
    scanf("%i",&r);

    // calculate area
    float n = ( (pi) * (r ** 2));

    printf("circle of circle is %f ",n);
    return 0;
}
