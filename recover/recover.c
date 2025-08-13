#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 2;
    }


    // Create a buffer for a block of data
    uint8_t buffer[512];

    char *filename = malloc(8);
    int number = 0;
    bool file_opened = false;
    bool first_file = false;
    FILE *img = NULL;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (!first_file)
            {
                first_file = true;
            }

            if (file_opened)
            {
                fclose(img);
                file_opened = false;
            }

            sprintf(filename, "%03i.jpg", number);

            //open file for writing data
            img = fopen(filename, "w");
            if (img == NULL)
            {
                printf("Could not open image file.\n");
                return 3;
            }

            file_opened = true;
            //write first 512 bytes
            fwrite(buffer, sizeof(uint8_t), 512, img);
            number++;
        }
        else
        {
            if (first_file)
            {
                //write 512 bytes
                fwrite(buffer, sizeof(uint8_t), 512, img);
            }
        }
    }

    if (file_opened)
    {
        // closing file
        fclose(img);
    }

    free(filename);
    fclose(card);
}
