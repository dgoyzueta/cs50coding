#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool validate_key(string character);
char get_cipher_char(char letter, string txt_key);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        if (!validate_key(argv[1]))
        {
            printf("Key must contain 26 unique letters of the alphabet.\n");
            return 1;
        }

        string plain_text = get_string("plaintext: ");

        printf("ciphertext: ");
        int k = 0;
        while (plain_text[k] != '\0')
        {
            printf("%c", get_cipher_char(plain_text[k], argv[1]));
            k++;
        }
        printf("\n");
        return 0;
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
}


bool validate_key(string key)
{
    char alpha_upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    if (strlen(key) != 26)
    {
        return false;
    }

    int k = 0, dupes = 0;

    while (alpha_upper[k] != '\0')
    {
        int m = 0;
        bool first_find = false;

        while (key[m] != '\0')
        {
            if (!isalpha(key[m]))
            {
                return false;
            }
            if (toupper(key[m]) == alpha_upper[k])
            {
                if (first_find)
                {
                    dupes++;
                }
                first_find = true;
            }
            if (dupes > 0)
            {
                return false;
            }
            m++;
        }
        k++;
    }
    return true;
}


char get_cipher_char(char letter, string txt_key)
{
    int i = 0;
    char alpha_upper[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    while (alpha_upper[i] != '\0')
    {
        if (toupper(letter) == alpha_upper[i])
        {
            if (islower(letter))
            {
                return tolower(txt_key[i]);
            }
            else
            {
                return toupper(txt_key[i]);
            }
        }
        i++;
    }
    return letter;
}
