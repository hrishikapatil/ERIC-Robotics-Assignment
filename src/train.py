from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Train the model
model.train(
    data="dataset/data.yaml",
    epochs=5,
    imgsz=320,
    batch=4,
    device="cpu",
    workers=2,
    project="./results",
    name="yolo_training"
)

print("Training completed!")