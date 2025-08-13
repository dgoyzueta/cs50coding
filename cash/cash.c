#include <cs50.h>
#include <stdio.h>

int get_amount(void);
int get_coins(int dollars);

int main(void)
{
    int amount = get_amount();
    printf("%i\n", get_coins(amount));
}

int get_amount(void)
{
    int n = 0;
    do
    {
        n = get_int("Change owed: ");
    }
    while (n < 0);

    return n;

}

int get_coins(int dollars)
{
    int quarters = 0;
    int after_quarters = 0;
    int dimes = 0;
    int after_dimes = 0;
    int nickels = 0;
    int after_nickels = 0;

    quarters = dollars / 25;
    after_quarters = dollars % 25;

    if (after_quarters > 0)
    {
        dimes = after_quarters / 10;
        after_dimes = after_quarters % 10;

        if (after_dimes > 0)
        {
            nickels = after_dimes / 5;
            after_nickels = after_dimes % 5;
        }
    }

    return quarters + dimes + nickels + after_nickels;

}
