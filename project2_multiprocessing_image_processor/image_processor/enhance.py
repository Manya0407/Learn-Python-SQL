from PIL import ImageEnhance

def enhance_image(image):
    """Enhance image brightness and sharpness."""
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.2)  # Increase brightness by 20%

    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(1.5)  # Increase sharpness by 50%

    return image
