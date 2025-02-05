import pytest
from PIL import Image
from image_processor.filter import apply_filter

@pytest.fixture
def sample_image():
    return Image.new("RGB", (100, 100), color="red")

def test_grayscale_filter(sample_image):
    gray_image = apply_filter(sample_image, "grayscale")
    assert gray_image.mode == "L"

def test_invalid_filter(sample_image):
    with pytest.raises(ValueError):
        apply_filter(sample_image, "unknown")
