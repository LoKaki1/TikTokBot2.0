import re
import textwrap
import os

from PIL import Image, ImageDraw, ImageFont
from rich.progress import track


def draw_multiple_line_text(image, text, font, text_color, padding, wrap=50):
    """
    Draw multiline text over given image
    """
    draw = ImageDraw.Draw(image)
    Fontperm = font.getsize(text)
    image_width, image_height = image.size
    lines = textwrap.wrap(text, width=wrap)
    y = (image_height / 2) - (
        ((Fontperm[1] + (len(lines) * padding) / len(lines)) * len(lines)) / 2
    )
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y), line, font=font, fill=text_color)
        y += line_height + padding


# theme=bgcolor,reddit_obj=reddit_object,txtclr=txtcolor
def imagemaker(theme, texts, txtclr, title, padding=5):
    """
    Render Images for video
    """
    tfont = ImageFont.truetype(os.path.join("../../fonts", "Roboto-Bold.ttf"), 27)  # for title
    font = ImageFont.truetype(
        os.path.join("../../fonts", "Roboto-Regular.ttf"), 20
    )  # for despcription|comments
    size = (500, 176)

    image = Image.new("RGBA", size, theme)
    draw = ImageDraw.Draw(image)

    # for title
    if len(title) > 40:
        draw_multiple_line_text(image, title, tfont, txtclr, padding, wrap=30)
    else:

        front_perm = tfont.getsize(title)
        draw.text(
            ((image.size[0] - front_perm[0]) / 2, (image.size[1] - front_perm[1]) / 2),
            font=tfont,
            text=title,
        )  # (image.size[1]/2)-(Fontperm[1]/2)

    front_perm = font.getsize(texts)
    print(front_perm)
    draw.text(
        ((image.size[0] - front_perm[0]) / 2, (image.size[1] - front_perm[1]) / 2),
        font=font,
        text=texts,
    )  # (image.size[1]/2)-(Fontperm[1]/2)

    image.save(f"../../assets/comments/title2.png")


bgcolor = (13, 23, 32, 255)
txtcolor = (31, 22, 123, 255)

imagemaker(bgcolor, "noder dafasfdsfkjhdsalghfdgkjhfdlkjsg", txtcolor, "hitler")