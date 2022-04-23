#include<stdio.h>
int main()
{
    double M[12][12];
    double sum[][];
    int l;
    char t;
    scanf_s("%d", &l);
    scanf_s("%c", &t,1);
    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            scanf_s("%lf", &M[i][j]);
            if (i == l)
                sum += M[i][j];
        }
    }
    ;
    
    if (t == 'S')
        printf("%.1lf", sum);
    else
        printf("%.1lf", sum / 12.0);
   

    
    return 0;
}
