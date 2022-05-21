#include <stdio.h>



int main(void)
{
    int width;
    int height;

    printf("Enter width of triangle:");
    scanf("%d", &width);

    printf("Enter height of triangle:");
    scanf("%d", &height);

    float answer = (width * height) * 0.5;


    printf("Area is %f", answer);
    return 0;

}