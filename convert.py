import cv2
ascii_chars = '@#$%B&W8Mosh*+;:,. '

def convert(img):
    out = ""
    rows, cols, _ = img.shape
    for i in range(rows):
        for j in range(cols):
            out += pixel_to_char(img[i, j])
        out += '\n'
    
    return out

def pixel_to_char(pixel) -> str:
    brightness = int(0.299 * pixel[2] + 0.587 * pixel[1] + 0.114 * pixel[0])
    index = int((brightness / 255) * (len(ascii_chars) - 1))
    return ascii_chars[index]