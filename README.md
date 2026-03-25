# Ascii Converter

## Features

Converts any image into ASCII characters, simply import your image and then copy the ASCII from the textbox.

## Technologies

- Python
- OpenCV
- Tkinter

## How it works

- Scales down the given picture to a factor of 0.1x
- Loops through each pixel in the image
- Converts the RGB values of the pixel into a brightness factor
- Decides on a character from a predefined string according to the brightness factor
- Does same for all the pixels
- Displays the output in a text field

## Screenshots

![Sebastian Vettel at the Indian Grand Prix 2013][./pics/seb.png]
![Arch Linux Logo][./pics/arch.png]
