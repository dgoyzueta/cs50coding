#include <stdio.h>

int main(void)
{
    int n[100];

    for (int i = 0; i < 100; i++)
    {
        printf("Value in memory: %i - Memory address: %p\n", n[i], &n[i]);
    }
    return 0;
}
