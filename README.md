# ERIC Robotics Assignment - Hrishika Patil
## Object Detection, Distance Estimation and Edge Optimization

### 1. Project Overview

This project implements a computer vision pipeline for detecting navigation-relevant objects and estimating their distance from a camera/robot perspective.

The main target objects are:

- Traffic cones
- Barriers
- Stop signs

The project uses a YOLO-based object detection model with transfer learning and includes distance estimation and CPU inference optimization.

---

## 2. Objectives

The objectives of this project are:

1. Detect navigation-relevant objects from camera images.
2. Identify cones, barriers and stop signs.
3. Estimate the distance of each detected object.
4. Annotate the detected objects with their estimated distance.
5. Measure inference performance on CPU.
6. Improve inference speed using a lightweight input resolution.
7. Maintain a modular and reusable implementation.

---

## 3. Technologies Used

- Python
- YOLO11
- Ultralytics
- OpenCV
- NumPy
- PyTorch
- Pandas
- Matplotlib
- VS Code
- Windows
- CPU-based inference

---

## 4. Project Structure

```text
ERIC_Robotics_Assignment/
│
├── data/
│   ├── images/
│   └── labels/
│
├── models/
│
├── results/
│   ├── detection/
│   ├── distance/
│   └── optimization/
│
├── runs/
│   └── detect/
│       └── results/
│           └── yolo_training/
│               └── weights/
│                   └── best.pt
│
├── src/
│   ├── train.py
│   ├── detect.py
│   ├── distance.py
│   ├── inference.py
│   ├── optimize.py
│   └── utils.py
│
├── data.yaml
├── requirements.txt
├── README.md
└── yolo11n.pt


---

## 5. Detection and Distance Estimation

The project uses YOLO11 for object detection.

The inference pipeline:
1. Loads the trained YOLO model.
2. Processes validation images.
3. Detects relevant objects.
4. Filters the target classes.
5. Estimates object distance using bounding-box height.
6. Annotates the output images.
7. Saves the results in the `results/distance/` directory.

The target classes are:

- Cone
- Barrier
- Stop Sign

Distance is estimated using the pinhole-camera relationship:

Distance = (Real Object Height × Focal Length) / Pixel Height

The implementation uses approximate real-world object heights and a calibrated/assumed focal length.

---

## 6. CPU Performance and Optimization

The system was evaluated on a CPU-only laptop.

### Original Configuration

- Input resolution: 640 × 640
- Model: YOLO11n
- Device: CPU
- Measured CPU FPS: **3.36 FPS**

### Optimized Configuration

The input resolution was reduced from 640 × 640 to 320 × 320 to reduce computational cost.

- Input resolution: 320 × 320
- Model: YOLO11n
- Device: CPU
- Measured CPU FPS: **5.92 FPS**

### Performance Comparison

| Configuration | Input Size | CPU FPS |
|---|---:|---:|
| Original | 640 × 640 | 7.07 |
| Optimized | 320 × 320 | 14.27 |

The measured speed improvement was approximately:

**2.02×**

This demonstrates that reducing the input resolution can significantly improve inference speed on CPU-based edge hardware.

---

## 7. Results

The inference and distance-estimation pipeline was successfully executed on the validation dataset.

The generated results are stored in:

```text
results/distance/

---

## 8. Limitations

- Distance estimates are approximate because object dimensions and camera focal length are estimated.
- Performance depends on the CPU hardware and input image characteristics.
- Lower input resolution improves speed but may reduce detection accuracy for small objects.
- The system is intended as a practical demonstration of object detection, distance estimation and CPU optimization rather than a production-grade autonomous navigation system.

---

## 9. Conclusion

This project demonstrates a modular computer vision pipeline for navigation-relevant object detection, distance estimation and CPU inference optimization.

The system successfully performs object detection and distance estimation and demonstrates a measured improvement from ** 3.36 FPS to 5.92 FPS**, corresponding to approximately **2.45× speed improvement** after reducing the input resolution from 640 × 640 to 320 × 320.

---

## Contact Info

- Name: Hrishika Patil
- Phone: 7058439880
- Email: hrishi0912patil@gmail.com