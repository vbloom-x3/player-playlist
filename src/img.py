import sys
import os
from PIL import Image
from colorama import Style, init

init(autoreset=True)

# Character set for ASCII representation
ASCII_CHARS = "▒▒▒▒▒▒▒▒▒ "  # dark to light

def resize_image(image, new_width=25):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.50)  # adjust for font aspect ratio
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    return "".join([ASCII_CHARS[pixel * (len(ASCII_CHARS)-1) // 255] for pixel in pixels])

def colorize_ascii(image, ascii_str):
    """Apply true color to each ASCII character using RGB values from original image."""
    colored_str = ""
    pixels = list(image.convert("RGB").getdata())
    width = image.width
    for i, char in enumerate(ascii_str):
        r, g, b = pixels[i]
        colored_str += f"\033[38;2;{r};{g};{b}m{char}{Style.RESET_ALL}"
        if (i + 1) % width == 0:
            colored_str += "\n"
    return colored_str

def image_to_ascii(image_path, new_width=50):
    """Convert an image to colored ASCII art."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    try:
        image = Image.open(image_path)
    except Exception as e:
        raise RuntimeError(f"Unable to open image: {e}")

    image = resize_image(image, new_width)
    image_gray = grayify(image)
    ascii_str = pixels_to_ascii(image_gray)
    return colorize_ascii(image, ascii_str)

def save_ascii_to_file(ascii_art, file_path="ascii_art.txt"):
    """Save the ASCII art to a text file."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(ascii_art)

# CLI entry point
if __name__ == "__main__":
    # Read file from argument or stdin
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = sys.stdin.readline().strip()

    if not os.path.exists(path):
        print("0x001F")  # error code like your original
        sys.exit(1)

    art = image_to_ascii(path, new_width=25)  # small size for CLI
    if art:
        print(art)
        save_ascii_to_file(art)
