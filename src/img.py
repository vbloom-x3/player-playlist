import sys
import os
from PIL import Image
from colorama import Style, init

init(autoreset=True)

# ASCII_CHARS = "@%#*+=-:. "
ASCII_CHARS = "▒▒▒▒▒▒▒▒▒ "
# ASCII_CHARS = "⣿⣿⣿⣿⣿⣿⣿⣿⣿ "
def resize_image(image, new_width=25):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.50)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    chars = "".join([ASCII_CHARS[pixel * (len(ASCII_CHARS)-1) // 255] for pixel in pixels])
    return chars

def colorize_ascii(image, ascii_str):
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
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image: {e}")
        return

    image = resize_image(image, new_width)
    image_gray = grayify(image)
    ascii_str = pixels_to_ascii(image_gray)
    ascii_art = colorize_ascii(image, ascii_str)
    return ascii_art

if __name__ == "__main__":
    
# Read file from argument or stdin
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = sys.stdin.readline().strip()

    if not os.path.exists(path):
        print("0x001F")

    art = image_to_ascii(path, new_width=25)  # smol size
    if art:
        print(art)
        with open("ascii_art.txt", "w", encoding="utf-8") as f:
            f.write(art)
