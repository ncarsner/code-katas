from rembg import remove
from PIL import Image


def remove_background(image_path, output_path):
    processed_image = Image.open(image_path).convert("RGBA")
    output_image = remove(processed_image)

    output_image.save(output_path)
    print(f"Background removed from {image_path} and saved to {output_path}")


if __name__ == "__main__":
    file_name = "dog2"
    image_path = rf"C:\Users\kmlee\Downloads\{file_name}.jpg"
    output_path = rf"C:\Users\kmlee\Downloads\{file_name}_nobg.png"

    remove_background(image_path, output_path)
