from ultralytics import YOLO
import cv2
import os

from distance import get_distance_label


MODEL_PATH = r"runs\detect\results\yolo_training-4\weights\best.pt"
IMAGE_PATH = r"dataset\valid\images"


def run_inference():

    model = YOLO(MODEL_PATH)

    results = model.predict(
        source=IMAGE_PATH,
        save=False,
        conf=0.25
    )

    output_folder = r"results\distance"
    os.makedirs(output_folder, exist_ok=True)

    for result in results:

        image = result.orig_img.copy()

        if result.boxes is None:
            continue

        for box in result.boxes:

            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            allowed_classes = ["cone", "barrier", "stop_sign", "trafficcone", "fencebarriers", "stopsign"]
            if class_name.lower() not in allowed_classes:
                continue

            if class_name.lower() not in ["trafficcone", "fencebarriers", "stopsign"]:
                continue
            if class_name.lower() == "trafficcone":
                class_name = "cone"
            elif class_name.lower() == "fencebarriers":
                class_name = "barrier"
            elif class_name.lower() == "stopsign":
                class_name = "stop_sign"

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            pixel_height = y2 - y1

            distance_text = get_distance_label(
                class_name,
                pixel_height
            )

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                image,
                distance_text,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        filename = os.path.basename(result.path)

        output_path = os.path.join(
            output_folder,
            filename
        )

        cv2.imwrite(output_path, image)

    print("Distance estimation completed!")
    print("Results saved in:", output_folder)


if __name__ == "__main__":
    run_inference()