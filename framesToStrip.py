from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def resize_images(image_paths, target_height):
    resized_images = []
    for image_path in image_paths:
        image = Image.open(image_path)
        aspect_ratio = image.width / image.height
        target_width = int(target_height * aspect_ratio)
        resized_image = image.resize((target_width, target_height))
        resized_images.append(resized_image)
    return resized_images

def MakeCartoonStrip(image_paths):
    target_height = 400  # Desired height for all images

    # Resize images to the target height while maintaining aspect ratio
    resized_images = resize_images(image_paths, target_height)

    # Create a new figure for plotting
    fig, axes = plt.subplots(1, len(image_paths), figsize=(len(image_paths) * 5, 5))

    for ax, resized_image, image_path in zip(axes, resized_images, image_paths):
        ax.imshow(np.array(resized_image))
        ax.axis('off')  # Turn off axis labels
        ax.set_title(image_path)  # Set title as image path

    plt.show()

# Example usage:
testi_strippi = ["frameSet/0-0.jpg", "frameSet/463-1.jpg", "frameSet/0-0.jpg"]
MakeCartoonStrip(testi_strippi)
