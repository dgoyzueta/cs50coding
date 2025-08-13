#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>

int get_count_letters(string txt);
int get_count_words(string txt);
int get_count_sentences(string txt);
float get_reading_level(int l, int w, int s);

int main(void)
{
    string text = get_string("Enter text to evaluate US reading level: ");

    int num_letters = get_count_letters(text);
    int num_words = get_count_words(text);
    int num_sentences = get_count_sentences(text);
    float reading_level = get_reading_level(num_letters, num_words, num_sentences);

    if (reading_level < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (reading_level > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(reading_level));
    }
}


int get_count_letters(string txt)
{
    int k = 0, count = 0;
    while (txt[k] != '\0')
    {
        if (isalpha(txt[k]))
        {
            count++;
        }
        k++;
    }
    return count;
}


int get_count_words(string txt)
{
    int k = 0, count = 0;
    bool at_least_one_space = false;

    while (txt[k] != '\0')
    {
        if (txt[k] == ' ')
        {
            count++;
            at_least_one_space = true;
        }
        k++;
    }
    if (at_least_one_space)
    {
        count++;
        return count;
    }
    else
    {
        return 1;
    }
}


int get_count_sentences(string txt)
{
    int k = 0, count = 0;
    while (txt[k] != '\0')
    {
        if (txt[k] == '.' || txt[k] == '!' || txt[k] == '?')
        {
            count++;
        }
        k++;
    }
    return count;
}


float get_reading_level(int l, int w, int s)
{
    // Computes the Coleman-Liau index for US reading level based on the number of letters,
    // words and sentences in a text
    float index = (0.0588 * (((float) l / (float) w) * 100)) - (0.296 * (((float) s / (float) w) * 100)) - 15.8;

    return index;
}
