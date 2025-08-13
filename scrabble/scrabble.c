#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string get_winner(string t1, string t2);
int get_letter_value(char single_letter);

int main(void) {
    string text1 = get_string("Enter text No 1: ");
    string text2 = get_string("Enter text No 2: ");

    string winner = get_winner(text1, text2);

    printf("%s\n", winner);
}


string get_winner(string t1, string t2)
{
    int sum_text_1 = 0, sum_text_2 = 0;

    // Get sum of values for text 1
    for (int i = 0, length = strlen(t1); i < length; i++)
    {
        sum_text_1 += get_letter_value(t1[i]);
    }

    // Get sum of values for text 2
    for (int i = 0, length = strlen(t2); i < length; i++)
    {
        sum_text_2 += get_letter_value(t2[i]);
    }

    if (sum_text_1 > sum_text_2)
    {
        return "Player 1 wins!";
    }
    else if (sum_text_2 > sum_text_1)
    {
        return "Player 2 wins!";
    }
    else
    {
        return "Tie!";
    }
}

// Get value from letter of Alphabet according the predefined values
int get_letter_value(char single_letter)
{
    char letter[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int value[] = {1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};

    int k = 0;
    while (letter[k] != '\0')
    {
        if (toupper(single_letter) == letter[k])
        {
            return value[k];
        }
        k++;
    }
    return 0;
}
