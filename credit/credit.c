#include <cs50.h>
#include <stdio.h>
#include <math.h>

long get_number(void);
bool validate_credit_card(long cc_number);
int get_number_digits(long n);
string get_cc_type(long cc_number);


int main(void)
{
    long number = get_number();
    bool valid_cc = validate_credit_card(number);

    if (valid_cc)
    {
        printf("%s\n", get_cc_type(number));
    }
    else
    {
        printf("INVALID\n");
    }
}


long get_number(void)
{
    long n = 0;
    do
    {
        n = get_long("Enter credit card number: ");
    }
    while (n < 0);

    return n;
}


bool validate_credit_card(long cc_number)
{
    int digits = get_number_digits(cc_number);

    long prev = 0;
    int d = 0;
    long divisor = 1;
    bool by_2 = false;
    int final_sum = 0;

    for (d = 1; d <= digits; d++)
    {
        if (by_2)
        {
            long temp = 0;

            temp = (((cc_number % (divisor * 10)) - prev) / divisor) * 2;

            if (temp >= 10)
            {
                final_sum = final_sum + (temp / 10) + (temp % 10);
            }
            else
            {
                final_sum = final_sum + temp;
            }

            by_2 = false;
        }
        else
        {
            final_sum = final_sum + (((cc_number % (divisor * 10)) - prev) / divisor);
            by_2 = true;
            prev = cc_number % (divisor * 10);
        }

        divisor = divisor * 10;
    }

    if (final_sum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}


int get_number_digits(long n)
{
    if (n == 0)
    {
        return 1;
    }

    int count = 0;
    while (n > 0)
    {
        n = n / 10;
        count++;
    }
    return count;
}


string get_cc_type(long cc_number)
{
    long first_2_digits = 0;
    long divisor = 0;
    int num_digits = get_number_digits(cc_number);
    divisor = pow(10, num_digits - 2);

    first_2_digits = cc_number / divisor;

    if ((first_2_digits == 34 || first_2_digits == 37) && num_digits == 15)
    {
        return "AMEX";
    }
    else if ((first_2_digits >= 51 && first_2_digits <= 55) && num_digits == 16)
    {
        return "MASTERCARD";
    }
    else if ((first_2_digits / 10) == 4 && (num_digits == 13 || num_digits == 16))
    {
        return "VISA";
    }
    else
    {
        return "INVALID";
    }
}
