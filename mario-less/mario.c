#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_pyramid(int h);

int main(void)
{
    int height = get_height();
    print_pyramid(height);
}

int get_height(void)
{
    int n = 0;
    do
    {
        n = get_int("Height of pyramid: ");
    }
    while (n <= 0);

    return n;
}

void print_pyramid(int h)
{
    for (int row = 1; row <= h; row++)
    {
        for (int blank = 1; blank < (h-row+1); blank++)
        {
            printf(" ");
        }

        for (int hash = 1; hash <= row; hash++)
        {
            printf("#");
        }

        printf("\n");
    }
}
