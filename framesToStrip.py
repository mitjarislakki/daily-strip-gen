import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def display_images_with_same_height(image_paths, target_height=300):
    num_images = len(image_paths)
    fig, ax = plt.subplots(1, num_images, figsize=(num_images * 5, 5))

    for i, path in enumerate(image_paths):
        img = Image.open(path)
        aspect_ratio = img.width / img.height
        target_width = int(target_height * aspect_ratio)
        img = img.resize((target_width, target_height))

        ax[i].imshow(img)
        ax[i].axis('off')
        ax[i].set_title(f'Image {i+1}')

    plt.tight_layout()
    plt.show()
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def display_images_with_same_height(image_paths, target_height=200):
    num_images = len(image_paths)
    fig, ax = plt.subplots(1, num_images, figsize=(num_images * 5, 5))

    for i, path in enumerate(image_paths):
        img = Image.open(path)
        aspect_ratio = img.width / img.height
        target_width = int(target_height * aspect_ratio)
        img = img.resize((target_width, target_height))

        ax[i].imshow(img)
        ax[i].axis('off')
        ax[i].set_title(f'Image {i+1}')

    plt.tight_layout()
    plt.show()


# Example usage
image_paths = ['frameSet/0-0.jpg', 'frameSet/15-0.jpg', 'frameSet/12-1.jpg']  # Paths to your images
display_images_with_same_height(image_paths)
