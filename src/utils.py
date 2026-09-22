import os
import time


def check_file_exists(file_path):
    """Check whether a file exists."""
    return os.path.exists(file_path)


def measure_fps(model, image_path, runs=10, imgsz=640):
    """Measure average inference FPS."""
    
    # Warm-up
    model(image_path, imgsz=imgsz, verbose=False)

    start_time = time.time()

    for _ in range(runs):
        model(image_path, imgsz=imgsz, verbose=False)

    total_time = time.time() - start_time

    fps = runs / total_time

    return fps