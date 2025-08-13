// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

bool case_insensitive_compare(const char *str1, const char *str2);

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

unsigned int number_of_words = 0;

// Hashes word to a number
unsigned int hash(const char *word)
{
    return toupper(word[0]) - 'A';
}


bool case_insensitive_compare(const char *str1, const char *str2)
{
    // Compare strings in a case-insensitive manner
    while (*str1 && *str2)
    {
        if (tolower((unsigned char)*str1) != tolower((unsigned char)*str2))
        {
            return false;
        }
        str1++;
        str2++;
    }
    return *str1 == *str2;
}


// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    for (int i = 0; i < N; i++)
    {
        node *current = table[i];
        while (current != NULL)
        {
            if (case_insensitive_compare(current->word, word))
            {
                return true;
            }
            current = current->next;
        }
    }
    return false;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Initialize the hash table to NULL
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }

    // Buffer to hold each word + 1 for newline and 1 for null terminator
    char buffer[LENGTH + 2];

    // Read each word in the file
    while (fgets(buffer, sizeof(buffer), source) != NULL)
    {
        // Remove newline character, if present
        size_t len = strlen(buffer);
        if (len > 0 && buffer[len - 1] == '\n')
        {
            buffer[len - 1] = '\0';
        }

        // Add each word to the hash table
        node *newNode = malloc(sizeof(node));
        if (newNode == NULL)
        {
            fclose(source);
            return false;
        }

        // Copy the word into the new node
        strncpy(newNode->word, buffer, LENGTH);
        newNode->word[LENGTH] = '\0';  // Ensure null-termination

        // Insert the new node at the beginning of the linked list for that index
        unsigned int index = hash(newNode->word);
        newNode->next = table[index];
        table[index] = newNode;

        number_of_words++;
    }

    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return number_of_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *current = table[i];
        while (current != NULL)
        {
            node *temp = current;
            current = current->next;
            free(temp);
        }
    }
    return true;
}
