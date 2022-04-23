#include<stdio.h>
int main()
{
    double M[12][12];
    double sum = 0;
    int l;
    char t;
    
    scanf_s("%c", &t);
   

    if (t == 'S')
        printf("%.1lf", sum);
    else
        printf("%.1lf", sum / 12.0);
    return 0;
}