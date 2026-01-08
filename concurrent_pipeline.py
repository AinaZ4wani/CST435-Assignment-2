import os
import time
import numpy as np
from PIL import Image
from concurrent.futures import ProcessPoolExecutor
import filters

# --------------------------------
# Worker function (optimized)
# --------------------------------
def process_single_image(args):
    img_path, output_folder = args
    try:
        filename = os.path.basename(img_path)

        with Image.open(img_path) as img:
            arr = np.asarray(img.convert("RGB"))

            # IDENTICAL image processing pipeline
            arr = filters.grayscale_conversion(arr)
            arr = filters.gaussian_blur(arr)
            arr = filters.sobel_edge_detection(arr)
            arr = filters.image_sharpening(arr)
            arr = filters.brightness_adjustment(arr, 1.2)

            Image.fromarray(arr).save(
                os.path.join(output_folder, f"proc_{filename}")
            )

        return True

    except Exception as e:
        return False


# --------------------------------
# Optimized concurrent.futures run
# --------------------------------
def run_test(image_list, output_dir, num_workers):
    tasks = [(p, output_dir) for p in image_list]

    start_time = time.time()

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        # map() is MUCH faster than submit + as_completed
        list(executor.map(
            process_single_image,
            tasks,
            chunksize=max(1, len(tasks) // (num_workers * 4))
        ))

    return time.time() - start_time