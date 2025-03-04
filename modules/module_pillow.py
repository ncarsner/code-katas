from PIL import Image, ImageDraw, ImageFont
from typing import Tuple


def open_image(file_path: str) -> Image.Image:
    """
    Open an image file and return the Image object.

    :param file_path: Path to the image file.
    :return: Image object.
    """
    try:
        img = Image.open(file_path)
        print(f"Image opened successfully: {file_path}")
        return img
    except Exception as e:
        print(f"Error opening image: {e}")
        raise


def resize_image(img: Image.Image, size: Tuple[int, int]) -> Image.Image:
    """
    Resize the image to the specified size.

    :param img: Image object to resize.
    :param size: New size as a tuple (width, height).
    :return: Resized Image object.
    """
    resized_img = img.resize(size)
    print(f"Image resized to: {size}")
    return resized_img


def add_text_to_image(
    img: Image.Image,
    text: str,
    position: Tuple[int, int],
    font_path: str,
    font_size: int,
) -> Image.Image:
    """
    Add text to the image at the specified position.

    :param img: Image object to add text to.
    :param text: Text to add to the image.
    :param position: Position to add the text (x, y).
    :param font_path: Path to the .ttf font file.
    :param font_size: Size of the font.
    :return: Image object with text added.
    """
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        print(f"Error loading font: {e}")
        raise

    draw.text(position, text, font=font, fill="white")
    print(f"Text '{text}' added to image at position {position}")
    return img


def save_image(img: Image.Image, save_path: str) -> None:
    """
    Save the image to the specified path.

    :param img: Image object to save.
    :param save_path: Path to save the image file.
    """
    try:
        img.save(save_path)
        print(f"Image saved successfully: {save_path}")
    except Exception as e:
        print(f"Error saving image: {e}")
        raise


if __name__ == "__main__":

    image_path = "example.jpg"
    font_path = "arial.ttf"
    output_path = "output.jpg"

    # Open an image
    image = open_image(image_path)

    # Resize the image
    resized_image = resize_image(image, (800, 600))

    # Add text to the image
    image_with_text = add_text_to_image(
        resized_image, "Hello, World!", (50, 50), font_path, 36
    )

    # Save the modified image
    save_image(image_with_text, output_path)
