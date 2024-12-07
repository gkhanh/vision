import math

from src.camera_calibration.camera_calibration import AxisMapper


def calculate_deviation(reference_axis, camera_points):
    """
    Calculate the angular deviation of the camera's axes from the reference axes.

    Args:
        reference_axis (dict): Points defining the reference axes.
                              Must include keys 'y_axis' and 'x_axis' with point tuples.
        camera_points (dict): Points representing the camera's axes.
                              Must include keys 'y_axis' and 'x_axis' with point tuples.

    Returns:
        tuple: (alpha, beta) where
               alpha is the deviation of the camera's Y-axis from the reference Y-axis,
               beta is the deviation of the camera's X-axis from the reference X-axis.
    """
    # Reference Y-axis points
    ref_y_start, ref_y_end = reference_axis['y_axis']
    # Camera Y-axis points
    cam_y_start, cam_y_end = camera_points['y_axis']

    # Calculate reference Y-axis angle
    ref_y_angle = math.degrees(math.atan2(ref_y_end[0] - ref_y_start[0],
                                          ref_y_start[1] - ref_y_end[1]))

    # Calculate camera Y-axis angle
    cam_y_angle = math.degrees(math.atan2(cam_y_end[0] - cam_y_start[0],
                                          cam_y_start[1] - cam_y_end[1]))

    # Deviation for Y-axis (alpha)
    alpha = cam_y_angle - ref_y_angle

    # Reference X-axis points
    ref_x_start, ref_x_end = reference_axis['x_axis']
    # Camera X-axis points
    cam_x_start, cam_x_end = camera_points['x_axis']

    # Calculate reference X-axis angle
    ref_x_angle = math.degrees(math.atan2(ref_x_end[0] - ref_x_start[0],
                                          ref_x_end[1] - ref_x_start[1]))

    # Calculate camera X-axis angle
    cam_x_angle = math.degrees(math.atan2(cam_x_end[0] - cam_x_start[0],
                                          cam_x_end[1] - cam_x_start[1]))

    # Deviation for X-axis (beta)
    beta = cam_x_angle - ref_x_angle

    return alpha, beta

# Example data for the reference axis and camera system
reference_axis = {
    'y_axis': [(0, 0), (0, 1)],  # Points defining the reference Y-axis
    'x_axis': [(0, 0), (1, 0)],  # Points defining the reference X-axis
}

camera_points = {
    'y_axis': [(1, 3), (4, 7)],  # Points defining the camera's Y-axis
    'x_axis': [(4, 7), (8, 6)],  # Points defining the camera's X-axis
}

mapper = AxisMapper()
mapper.add_points(camera_x=camera_points['x_axis'][0][0], camera_y=camera_points['x_axis'][0][1], manipulator_x=reference_axis['x_axis'][0][0], manipulator_y=reference_axis['x_axis'][0][1])
mapper.add_points(camera_x=camera_points['x_axis'][0][0], camera_y=camera_points['x_axis'][0][1], manipulator_x=reference_axis['x_axis'][0][0], manipulator_y=reference_axis['x_axis'][0][1])
mapper.add_points(camera_x=camera_points['x_axis'][0][0], camera_y=camera_points['x_axis'][0][1], manipulator_x=reference_axis['x_axis'][0][0], manipulator_y=reference_axis['x_axis'][0][1])

# Compute the deviations
alpha, beta = calculate_deviation(reference_axis, camera_points)

# Print the results
print(f"Alpha (Y-axis deviation): {alpha:.2f} degrees")
print(f"Beta (X-axis deviation): {beta:.2f} degrees")
