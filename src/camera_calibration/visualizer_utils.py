import matplotlib.pyplot as plt

# Visualizes all three axis maps together: Camera Axis Map, Manipulator Axis Map, and Merged Axis Map.
# def visualize_full_axis_maps(camera_points, manipulator_points, transformed_points):
#
#     plt.figure(figsize=(15, 5))
#
#     # Camera Axis Map (Red Points)
#     plt.subplot(1, 3, 1)
#     camera_x, camera_y = zip(*camera_points)
#     plt.scatter(camera_x, camera_y, color="red", label="Camera Points")
#     for i, (x, y) in enumerate(camera_points):
#         plt.text(x + 2, y + 2, f"C{i + 1}", color="red")
#     plt.title("Camera Axis Map (Red Points)")
#     plt.axhline(0, color="gray", linestyle="--")
#     plt.axvline(0, color="gray", linestyle="--")
#     plt.xlabel("X Axis (pixels)")
#     plt.ylabel("Y Axis (pixels)")
#     plt.grid()
#     plt.legend()
#
#     # Manipulator Axis Map (Blue Points)
#     plt.subplot(1, 3, 2)
#     manipulator_x, manipulator_y = zip(*manipulator_points)
#     plt.scatter(manipulator_x, manipulator_y, color="blue", label="Manipulator Points")
#     for i, (x, y) in enumerate(manipulator_points):
#         plt.text(x + 0.2, y + 0.2, f"M{i + 1}", color="blue")
#     plt.title("Manipulator Axis Map (Blue Points)")
#     plt.axhline(0, color="gray", linestyle="--")
#     plt.axvline(0, color="gray", linestyle="--")
#     plt.xlabel("X Axis (mm)")
#     plt.ylabel("Y Axis (mm)")
#     plt.grid()
#     plt.legend()
#
#     # Merged Axis Map: Manipulator and Transformed Camera Points
#     plt.subplot(1, 3, 3)
#     plt.title("Merged Axis Map: Manipulator and Transformed Camera Points")
#
#     # Manipulator Points
#     plt.scatter(manipulator_x, manipulator_y, color="blue", label="Manipulator Points")
#     for i, (x, y) in enumerate(manipulator_points):
#         plt.text(x + 0.2, y + 0.2, f"M{i + 1}", color="blue")
#
#     # Transformed Camera Points
#     transformed_x, transformed_y = zip(*transformed_points)
#     plt.scatter(transformed_x, transformed_y, color="green", label="Transformed Camera Points")
#     for i, (x, y) in enumerate(transformed_points):
#         plt.text(x + 0.2, y + 0.2, f"T{i + 1}", color="green")
#
#     plt.axhline(0, color="gray", linestyle="--")
#     plt.axvline(0, color="gray", linestyle="--")
#     plt.xlabel("X Axis (mm)")
#     plt.ylabel("Y Axis (mm)")
#     plt.grid()
#     plt.legend()
#
#     plt.tight_layout()
#     plt.show()

def visualize_combined_axis_map(manipulator_points, camera_points, transformed_points):
    """
    Visualize the combined axis map:
    - Manipulator axis (blue points).
    - Camera axis (red points).
    - Transformed points (green points in manipulator space).
    - Overlay the new camera axis derived from the second point.
    """
    plt.figure(figsize=(8, 8))

    # Plot Manipulator Points (Blue)
    manipulator_x, manipulator_y = zip(*manipulator_points)
    plt.scatter(manipulator_x, manipulator_y, color="blue", label="Manipulator Points")
    for i, (x, y) in enumerate(manipulator_points):
        plt.text(x + 0.2, y + 0.2, f"M{i + 1}", color="blue")

    # Plot Camera Points (Red)
    camera_x, camera_y = zip(*camera_points)
    plt.scatter(camera_x, camera_y, color="red", label="Camera Points")
    for i, (x, y) in enumerate(camera_points):
        plt.text(x + 0.2, y + 0.2, f"C{i + 1}", color="red")

    # Plot Transformed Points (Green)
    transformed_x, transformed_y = zip(*transformed_points)
    plt.scatter(transformed_x, transformed_y, color="green", label="Transformed Points")
    for i, (x, y) in enumerate(transformed_points):
        plt.text(x + 0.2, y + 0.2, f"T{i + 1}", color="green")

    # Draw the new camera axis (from the second point)
    second_point = manipulator_points[1]  # Second point becomes the origin
    x_axis = [second_point[0], second_point[0] + 10]  # X-axis direction
    y_axis = [second_point[1], second_point[1] - 10]  # Y-axis direction

    plt.plot([second_point[0], x_axis[0]], [second_point[1], x_axis[1]], 'r-', label="Camera X-axis (Red)")
    plt.plot([second_point[0], y_axis[0]], [second_point[1], y_axis[1]], 'g-', label="Camera Y-axis (Green)")

    # Formatting
    plt.axhline(0, color="gray", linestyle="--")
    plt.axvline(0, color="gray", linestyle="--")
    plt.title("Combined Axis Map")
    plt.xlabel("X Axis (mm)")
    plt.ylabel("Y Axis (mm)")
    plt.grid()
    plt.legend()
    plt.show()


