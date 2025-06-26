import colorsys
from typing import Tuple, List

"""
The `colorsys` module is useful for color manipulation, such as converting between color spaces (RGB, HSV, HLS, YIQ), for use in data visualization, dashboard theming, or color-based data segmentation. It provides functions to convert colors between different color spaces and generate visually distinct color palettes."""


def rgb_to_hsv(rgb: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """
    Convert an RGB color to HSV color space.

    Args:
        rgb: Tuple of (r, g, b), each in range [0.0, 1.0].

    Returns:
        Tuple of (h, s, v), each in range [0.0, 1.0].
    """
    return colorsys.rgb_to_hsv(*rgb)


def hsv_to_rgb(hsv: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """
    Convert an HSV color to RGB color space.

    Args:
        hsv: Tuple of (h, s, v), each in range [0.0, 1.0].

    Returns:
        Tuple of (r, g, b), each in range [0.0, 1.0].
    """
    return colorsys.hsv_to_rgb(*hsv)


def rgb_to_hls(rgb: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """
    Convert an RGB color to HLS color space.

    Args:
        rgb: Tuple of (r, g, b), each in range [0.0, 1.0].

    Returns:
        Tuple of (h, l, s), each in range [0.0, 1.0].
    """
    return colorsys.rgb_to_hls(*rgb)


def hls_to_rgb(hls: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """
    Convert an HLS color to RGB color space.

    Args:
        hls: Tuple of (h, l, s), each in range [0.0, 1.0].

    Returns:
        Tuple of (r, g, b), each in range [0.0, 1.0].
    """
    return colorsys.hls_to_rgb(*hls)


def rgb_to_yiq(rgb: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """
    Convert an RGB color to YIQ color space (used in TV/video).

    Args:
        rgb: Tuple of (r, g, b), each in range [0.0, 1.0].

    Returns:
        Tuple of (y, i, q), each in range [0.0, 1.0].
    """
    return colorsys.rgb_to_yiq(*rgb)


def yiq_to_rgb(yiq: Tuple[float, float, float]) -> Tuple[float, float, float]:
    """
    Convert a YIQ color to RGB color space.

    Args:
        yiq: Tuple of (y, i, q), each in range [0.0, 1.0].

    Returns:
        Tuple of (r, g, b), each in range [0.0, 1.0].
    """
    return colorsys.yiq_to_rgb(*yiq)


def generate_color_palette(n: int) -> List[Tuple[float, float, float]]:
    """
    Generate a palette of n visually distinct RGB colors using HSV color space.

    Args:
        n: Number of colors to generate.

    Returns:
        List of RGB tuples, each in range [0.0, 1.0].
    """
    palette = []
    for i in range(n):
        hue = i / n
        rgb = colorsys.hsv_to_rgb(hue, 0.7, 0.9)
        palette.append(rgb)
    return palette


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(
        int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
    )


if __name__ == "__main__":
    # Convert a business brand color from RGB to HSV and back
    brand_rgb = (0.2, 0.6, 0.8)  # a blue shade
    print("Original RGB:", brand_rgb, "| HEX:", rgb_to_hex(brand_rgb))
    hsv = rgb_to_hsv(brand_rgb)
    print("Converted to HSV:", hsv)
    rgb_back = hsv_to_rgb(hsv)
    print("Back to RGB:", rgb_back, "| HEX:", rgb_to_hex(rgb_back))

    # Generate a color palette for a dashboard with 5 categories
    palette = generate_color_palette(5)
    print("Generated color palette (RGB):")
    for idx, color in enumerate(palette):
        print(f"Category {idx+1}: {color} | HEX: {rgb_to_hex(color)}")

    # Convert RGB to HLS for adjusting lightness
    hls = rgb_to_hls(brand_rgb)
    print("RGB to HLS:", hls)
    # Lighten the color by increasing lightness
    lighter_hls = (hls[0], min(hls[1] + 0.2, 1.0), hls[2])
    lighter_rgb = hls_to_rgb(lighter_hls)
    print("Lightened RGB:", lighter_rgb, "| HEX:", rgb_to_hex(lighter_rgb))

    # Troubleshooting tip: Ensure all input values are floats in [0.0, 1.0]
    # If you have 8-bit RGB (0-255), normalize: r/255.0, g/255.0, b/255.0
