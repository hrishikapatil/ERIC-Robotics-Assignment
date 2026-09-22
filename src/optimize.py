from ultralytics import YOLO
import glob

from utils import measure_fps


# Load YOLO model
model = YOLO(r"models\best.pt")

# Select one test image
image_path = glob.glob(r"dataset\valid\images\*.jpg")[0]

print("Test image:", image_path)

# Original 640x640
fps_original = measure_fps(
    model,
    image_path,
    runs=10,
    imgsz=640
)

print(f"Original CPU FPS: {fps_original:.2f}")


# Optimized 320x320
fps_optimized = measure_fps(
    model,
    image_path,
    runs=10,
    imgsz=320
)

print(f"Optimized CPU FPS: {fps_optimized:.2f}")


# Calculate improvement
improvement = fps_optimized / fps_original

print(f"Speed improvement: {improvement:.2f}x")