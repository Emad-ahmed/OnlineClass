#include <stdio.h>

void First_Fit();
void Best_Fit();
void Worst_Fit();

int main()
{
    int number;
    printf("Which operation to perform:\n1.First fit\n2.Best fit\n3.Worst fit\n");
    printf("Enter an operation to choose: ");
    scanf("%d", &number);
    if(number == 1)
        First_Fit();
    else if(number == 2)
        Best_Fit();
    else
        Worst_Fit();
    return 0;
}

void First_Fit()
{
    int fragment[10], block[10], jobs[10], i, j, nb, nf, temp;
    int bf[10], ff[10];

    printf("\nNumber of blocks : ");
    scanf("%d", &nb);
    printf("Enter Number of files : ");
    scanf("%d", &nf);

    printf("\nEnter the size of the blocks:-\n");
    for(i = 1; i <= nb; i++)
    {
        printf("Block %d:\t", i);
        scanf("%d", &block[i]);
        bf[i] = 0;
    }
    printf("Enter file no:-\n");
    for(i = 1; i <= nf; i++)
    {
        printf("File %d:\t", i);
        scanf("%d", &jobs[i]);
    }

    for(i = 1; i <= nf; i++)
    {
        for(j = 1; j <= nb; j++)
        {
            if(bf[j] != 1)
            {
                temp = block[j] - jobs[i];
                if(temp >= 0)
                {
                    ff[i] = j;
                    break;
                }
            }
        }
        fragment[i] = temp;
        bf[ff[i]] = 1;
    }


    printf("\nFile No:\tFile Size:\tBlock No:\tBlock Size:\tFragment");
    for(i = 1; i <= nf; i++)
    {
        printf("\n%d\t\t%d\t\t%d\t\t%d\t\t%d", i, jobs[i], ff[i], block[ff[i]], fragment[i]);
    }
}

void Best_Fit()
{
    int fragment[10], b[10], f[10], i, j, nb, nf, temp, lowest = 10000;
    int bf[10], ff[10];

    printf("\nEnter the number of blocks:");
    scanf("%d", &nb);
    printf("Enter the number of files:");
    scanf("%d", &nf);
    printf("\nEnter the size of the blocks:-\n");
    for(i = 1; i <= nb; i++)
    {
        printf("Block %d:", i);
        scanf("%d", &b[i]);
    }
    printf("Enter file no:-\n");
    for(i = 1; i <= nf; i++)
    {
        printf("File %d:\t", i);
        scanf("%d", &f[i]);
    }

    for(i = 1; i <= nf; i++)
    {
        for(j = 1; j <= nb; j++)
        {
            if(bf[j] != 1)
            {
                temp = b[j] - f[i];
                if(temp >= 0)
                {
                    if(lowest > temp)
                    {
                        ff[i] = j;
                        lowest = temp;
                    }
                }
            }
        }
        fragment[i] = lowest;
        bf[ff[i]] = 1;
        lowest = 10000;
    }
    printf("\nFile No:\tFile Size:\tBlock No:\tBlock Size:\tFragment");
    for(i = 1; i <= nf; i++)
    {
        printf("\n%d\t\t%d\t\t%d\t\t%d\t\t%d", i, f[i], ff[i], b[ff[i]], fragment[i]);
    }
}

void Worst_Fit()
{
    int fragment[10], b[10], f[10], i, j, nb, nf, temp, highest = 0;
    int bf[10], ff[10];

    printf("\nEnter the number of blocks:");
    scanf("%d", &nb);
    printf("Enter the number of files:");
    scanf("%d", &nf);
    printf("\nEnter the size of the blocks:-\n");
    for(i = 1; i <= nb; i++)
    {
        printf("Block %d:", i);
        scanf("%d", &b[i]);
    }
    printf("Enter file no:-\n");
    for(i = 1; i <= nf; i++)
    {
        printf("File %d:\t", i);
        scanf("%d", &f[i]);
    }

    for(i = 1; i <= nf; i++)
    {
        for(j = 1; j <= nb; j++)
        {
            if(bf[j] != 1)
            {
                temp = b[j] - f[i];
                if(temp >= 0)
                {
                    if(highest <= temp)
                    {
                        ff[i] = j;
                        highest = temp;
                    }
                }
            }
        }
        fragment[i] = highest;
        bf[ff[i]] = 1;
        highest = 0;
    }
    printf("\nFile No:\tFile Size:\tBlock No:\tBlock Size:\tFragment");
    for(i = 1; i <= nf; i++)
    {
        printf("\n%d\t\t%d\t\t%d\t\t%d\t\t%d", i, f[i], ff[i], b[ff[i]], fragment[i]);
    }
}
