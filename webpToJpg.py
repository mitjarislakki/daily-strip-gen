import os
from PIL import Image

def convert_webp_to_jpg(input_path, output_path):
    try:
        img = Image.open(input_path)
        img.save(output_path, 'JPEG')
        print(f"Converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def convert_all_webp_to_jpg(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.webp'):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, os.path.splitext(filename)[0] + '.jpg')
            convert_webp_to_jpg(input_path, output_path)

# Replace 'input_directory' with the path to the directory containing .webp files
input_directory = 'imageSet/'
convert_all_webp_to_jpg(input_directory)

