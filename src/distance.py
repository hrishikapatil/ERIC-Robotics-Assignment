def estimate_distance(real_height, focal_length, pixel_height):
    """
    Estimate object distance using:
    Distance = (Real Height × Focal Length) / Pixel Height
    """

    if pixel_height <= 0:
        return None

    distance = (real_height * focal_length) / pixel_height
    return distance


def get_distance_label(class_name, pixel_height):
    """
    Estimate distance using approximate object heights.
    """

    focal_length = 700  # approximate camera focal length in pixels

    object_heights = {
        "cone": 0.30,
        "barrier": 1.00,
        "stop_sign": 0.75
    }

    class_name = class_name.lower()

    if "cone" in class_name:
        class_name = "cone"
    elif "barrier" in class_name:
        class_name = "barrier"
    elif "stop" in class_name:
        class_name = "stop_sign"

    if class_name not in object_heights:
        return f"{class_name}, distance not required"

    real_height = object_heights[class_name]

    distance = estimate_distance(
        real_height,
        focal_length,
        pixel_height
    )

    if distance is None:
        return f"{class_name}, unknown distance"

    return f"{class_name}, {distance:.2f} m"