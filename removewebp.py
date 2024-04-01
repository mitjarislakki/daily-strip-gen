import os

input_directory = 'imageSet/'

for filename in os.listdir(input_directory):
        if filename.endswith('.webp'):
                os.remove(os.path.join(input_directory, filename))