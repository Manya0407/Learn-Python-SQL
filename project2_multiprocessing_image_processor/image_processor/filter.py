from PIL import Image, ImageFilter

def apply_filter(image, filter_type="grayscale"):
    """Apply a selected filter to an image."""
    if filter_type == "grayscale":
        return image.convert("L")
    elif filter_type == "blur":
        return image.filter(ImageFilter.BLUR)
    elif filter_type == "sharpen":
        return image.filter(ImageFilter.SHARPEN)
    else:
        raise ValueError("Unknown filter type")
