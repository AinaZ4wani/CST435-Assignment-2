import os
import time
from concurrent.futures import ProcessPoolExecutor

from core.pipeline import process_image

INPUT_DIR = "data/images"
OUTPUT_DIR = "output/futures"

def worker(image_path):
    return process_image(image_path, OUTPUT_DIR)

def run(workers):
    images = [
        os.path.join(INPUT_DIR, img)
        for img in os.listdir(INPUT_DIR)
        if img.lower().endswith(".jpg")
    ]

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    start = time.time()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        list(executor.map(worker, images))
    end = time.time()

    return end - start

if __name__ == "__main__":
    for w in [1, 2]:
        t = run(w)
        print(f"Concurrent Futures | Workers: {w} | Time: {t:.2f}s")