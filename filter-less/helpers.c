#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take average of red, green, and blue
            float avg = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;
            // Update pixel values
            image[i][j].rgbtBlue = (BYTE) round(avg);
            image[i][j].rgbtGreen = (BYTE) round(avg);
            image[i][j].rgbtRed = (BYTE) round(avg);
        }
    }
}


// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Compute sepia values
            int sepiaRed = (int) round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = (int) round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = (int) round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            // Update pixel with sepia values
            image[i][j].rgbtBlue = (BYTE) sepiaBlue;
            image[i][j].rgbtGreen = (BYTE) sepiaGreen;
            image[i][j].rgbtRed = (BYTE) sepiaRed;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float result_blue = 0;
            float result_green = 0;
            float result_red = 0;

            int left = i - 1;
            int right = i + 1;
            int above = j - 1;
            int below = j + 1;

            if (left < 0 && above < 0) // Left upper corner
            {
                result_blue = (copy[i][j].rgbtBlue + copy[right][j].rgbtBlue + copy[i][below].rgbtBlue + copy[right][below].rgbtBlue) / 4.0;
                result_green = (copy[i][j].rgbtGreen + copy[right][j].rgbtGreen + copy[i][below].rgbtGreen + copy[right][below].rgbtGreen) / 4.0;
                result_red = (copy[i][j].rgbtRed + copy[right][j].rgbtRed + copy[i][below].rgbtRed + copy[right][below].rgbtRed) / 4.0;
            }
            else if (left >= 0 && right < width && above < 0) // Top side
            {
                result_blue = (copy[i][j].rgbtBlue + copy[left][j].rgbtBlue + copy[right][j].rgbtBlue + copy[left][below].rgbtBlue + copy[right][below].rgbtBlue + copy[i][below].rgbtBlue) / 6.0;
                result_green = (copy[i][j].rgbtGreen + copy[left][j].rgbtGreen + copy[right][j].rgbtGreen + copy[left][below].rgbtGreen + copy[right][below].rgbtGreen + copy[i][below].rgbtGreen) / 6.0;
                result_red = (copy[i][j].rgbtRed + copy[left][j].rgbtRed + copy[right][j].rgbtRed + copy[left][below].rgbtRed + copy[right][below].rgbtRed + copy[i][below].rgbtRed) / 6.0;
            }
            else if (right >= width && above < 0) // Right upper corner
            {
                result_blue = (copy[i][j].rgbtBlue + copy[left][j].rgbtBlue + copy[i][below].rgbtBlue + copy[left][below].rgbtBlue) / 4.0;
                result_green = (copy[i][j].rgbtGreen + copy[left][j].rgbtGreen + copy[i][below].rgbtGreen + copy[left][below].rgbtGreen) / 4.0;
                result_red = (copy[i][j].rgbtRed + copy[left][j].rgbtRed + copy[i][below].rgbtRed + copy[left][below].rgbtRed) / 4.0;
            }
           else if (left < 0 && above >= 0 && below < height) // Left side
            {
                result_blue = (copy[i][j].rgbtBlue + copy[right][j].rgbtBlue + copy[i][above].rgbtBlue + copy[i][below].rgbtBlue + copy[right][above].rgbtBlue + copy[right][below].rgbtBlue) / 6.0;
                result_green = (copy[i][j].rgbtGreen + copy[right][j].rgbtGreen + copy[i][above].rgbtGreen + copy[i][below].rgbtGreen + copy[right][above].rgbtGreen + copy[right][below].rgbtGreen) / 6.0;
                result_red = (copy[i][j].rgbtRed + copy[right][j].rgbtRed + copy[i][above].rgbtRed + copy[i][below].rgbtRed + copy[right][above].rgbtRed + copy[right][below].rgbtRed) / 6.0;
            }
            else if (left < 0 && below >= height) // Left lower corner
            {
                result_blue = (copy[i][j].rgbtBlue + copy[right][j].rgbtBlue + copy[i][above].rgbtBlue + copy[right][above].rgbtBlue) / 4.0;
                result_green = (copy[i][j].rgbtGreen + copy[right][j].rgbtGreen + copy[i][above].rgbtGreen + copy[right][above].rgbtGreen) / 4.0;
                result_red = (copy[i][j].rgbtRed + copy[right][j].rgbtRed + copy[i][above].rgbtRed + copy[right][above].rgbtRed) / 4.0;
            }
            else if (right >= width && below >= height) // Right lower corner
            {
                result_blue = (copy[i][j].rgbtBlue + copy[left][j].rgbtBlue + copy[i][above].rgbtBlue + copy[left][above].rgbtBlue) / 4.0;
                result_green = (copy[i][j].rgbtGreen + copy[left][j].rgbtGreen + copy[i][above].rgbtGreen + copy[left][above].rgbtGreen) / 4.0;
                result_red = (copy[i][j].rgbtRed + copy[left][j].rgbtRed + copy[i][above].rgbtRed + copy[left][above].rgbtRed) / 4.0;
            }
            else if (right >= width && above >= 0 && below < height) // Right side
            {
                result_blue = (copy[i][j].rgbtBlue + copy[left][j].rgbtBlue + copy[i][above].rgbtBlue + copy[i][below].rgbtBlue + copy[left][above].rgbtBlue + copy[left][below].rgbtBlue) / 6.0;
                result_green = (copy[i][j].rgbtGreen + copy[left][j].rgbtGreen + copy[i][above].rgbtGreen + copy[i][below].rgbtGreen + copy[left][above].rgbtGreen + copy[left][below].rgbtGreen) / 6.0;
                result_red = (copy[i][j].rgbtRed + copy[left][j].rgbtRed + copy[i][above].rgbtRed + copy[i][below].rgbtRed + copy[left][above].rgbtRed + copy[left][below].rgbtRed) / 6.0;
            }
            else if (left >= 0 && right < width && below >= height) // Bottom side
            {
                result_blue = (copy[i][j].rgbtBlue + copy[left][j].rgbtBlue + copy[right][j].rgbtBlue + copy[left][above].rgbtBlue + copy[right][above].rgbtBlue + copy[i][above].rgbtBlue) / 6.0;
                result_green = (copy[i][j].rgbtGreen + copy[left][j].rgbtGreen + copy[right][j].rgbtGreen + copy[left][above].rgbtGreen + copy[right][above].rgbtGreen + copy[i][above].rgbtGreen) / 6.0;
                result_red = (copy[i][j].rgbtRed + copy[left][j].rgbtRed + copy[right][j].rgbtRed + copy[left][above].rgbtRed + copy[right][above].rgbtRed + copy[i][above].rgbtRed) / 6.0;
            }
            else if (left >= 0 && right < width && below < height && above >= 0) // Within a 3x3 square
            {
                result_blue = (copy[i][j].rgbtBlue + copy[left][j].rgbtBlue + copy[right][j].rgbtBlue + copy[left][above].rgbtBlue + copy[right][above].rgbtBlue + copy[i][above].rgbtBlue + copy[left][below].rgbtBlue + copy[right][below].rgbtBlue + copy[i][below].rgbtBlue) / 9.0;
                result_green = (copy[i][j].rgbtGreen + copy[left][j].rgbtGreen + copy[right][j].rgbtGreen + copy[left][above].rgbtGreen + copy[right][above].rgbtGreen + copy[i][above].rgbtGreen + copy[left][below].rgbtGreen + copy[right][below].rgbtGreen + copy[i][below].rgbtGreen) / 9.0;
                result_red = (copy[i][j].rgbtRed + copy[left][j].rgbtRed + copy[right][j].rgbtRed + copy[left][above].rgbtRed + copy[right][above].rgbtRed + copy[i][above].rgbtRed + copy[left][below].rgbtRed + copy[right][below].rgbtRed + copy[i][below].rgbtRed) / 9.0;
            }

            image[i][j].rgbtBlue = (BYTE) round(result_blue);
            image[i][j].rgbtGreen = (BYTE) round(result_green);
            image[i][j].rgbtRed = (BYTE) round(result_red);

        }
    }
}
