import splitStrip
import os
import concurrent.futures
from multiprocessing import cpu_count
import time

max_workers = cpu_count - 1

def splitAllStrips(directory):
    startTime = time.time()
    image_paths = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith('.jpg')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(splitStrip.fetchPages, image_paths)
    print(f"Completed in {time.time() - startTime} seconds")

input_directory = 'imageSet/'
splitAllStrips(input_directory)