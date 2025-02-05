import pytest
from PIL import Image
from image_processor.resize import resize_image

@pytest.fixture
def sample_image():
    return Image.new("RGB", (200, 200), color="blue")

def test_resize(sample_image):
    resized = resize_image(sample_image, (100, 100))
    assert resized.size == (100, 100)
