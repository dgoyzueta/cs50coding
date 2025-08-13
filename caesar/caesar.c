#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

bool validate_number(string character);
char get_cipher(char letter, string txt_key);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        if (!validate_number(argv[1]))
        {
            printf("Argument must be zero or a positive number.\n");
            return 1;
        }

        string plain_text = get_string("plaintext: ");

        printf("ciphertext: ");
        int k = 0;
        while (plain_text[k] != '\0')
        {
            printf("%c", get_cipher(plain_text[k], argv[1]));
            k++;
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}


bool validate_number(string character)
{
    int i = 0;
    bool digit = true;
    while (character[i] != '\0')
    {
        if (!isdigit(character[i]))
        {
            digit = false;
        }
        i++;
    }
    return digit;
}


char get_cipher(char letter, string txt_key)
{
    char alpha_upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char alpha_lower[] = "abcdefghijklmnopqrstuvwxyz";

    int key = atoi(txt_key);
    int p = 0, cipher_position = 0;

    while (alpha_upper[p] != '\0')
    {
        if (letter == alpha_upper[p])
        {
            cipher_position = ((p + key) % 26);
            return alpha_upper[cipher_position];
        }
        p++;
    }

    p = 0;
    while (alpha_lower[p] != '\0')
    {
        if (letter == alpha_lower[p])
        {
            cipher_position = ((p + key) % 26);
            return alpha_lower[cipher_position];
        }
        p++;
    }

    return letter;
}
