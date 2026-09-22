from ultralytics import YOLO
import os

MODEL_PATH = r"models\best.pt"
IMAGE_PATH = r"dataset\valid\images"

def detect_objects(image_path, model_path=MODEL_PATH):
    """
    Detect objects using the trained YOLO model.
    """

    model = YOLO(model_path)

    results = model.predict(
        source=image_path,
        save=True,
        conf=0.25
    )

    return results


if __name__ == "__main__":

    if not os.path.exists(MODEL_PATH):
        print("ERROR: Trained model not found.")
        print(MODEL_PATH)
    else:
        print("Using trained model:")
        print(MODEL_PATH)

        print("\nRunning detection on validation images...")

        results = detect_objects(IMAGE_PATH)

        print("\nDetection completed!")
        print("Results saved in:")
        print(r"runs\detect\predict")