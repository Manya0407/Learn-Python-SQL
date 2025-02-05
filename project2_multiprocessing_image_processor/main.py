import os
import multiprocessing
from image_processor.filter import apply_filter
from image_processor.resize import resize_image
from image_processor.enhance import enhance_image
from PIL import Image

INPUT_FOLDER = "images/"
OUTPUT_FOLDER = "output/"

def process_image(image_name):
    """Load an image, process it, and save it."""
    img_path = os.path.join(INPUT_FOLDER, image_name)
    img = Image.open(img_path)

    img = resize_image(img, (800, 600))
    img = apply_filter(img, "grayscale")
    img = enhance_image(img)

    output_path = os.path.join(OUTPUT_FOLDER, image_name)
    img.save(output_path)
    print(f"✅ Processed {image_name}")

if __name__ == "__main__":
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    images = [f for f in os.listdir(INPUT_FOLDER) if f.endswith((".jpg", ".png"))]

    with multiprocessing.Pool() as pool:
        pool.map(process_image, images)

    print("🎉 Image processing completed!")
