import math
def calculate_alpha(firstPoint, secondPoint):
    """
    Calculate Alpha, the angle in degrees the camera's Y-axis deviates.

    Parameters:
    x1, y1, x2, y2: Coordinates of the first two points.

    Returns:
    float: Alpha in degrees.
    """
    x1, y1 = firstPoint
    x2, y2 = secondPoint
    return math.degrees(math.atan((x2 - x1) / (y1 - y2)))

def calculate_beta(firstPoint, secondPoint):
    """
    Calculate Beta, the angle in degrees the camera's X-axis deviates.

    Parameters:
    x2, y2, x3, y3: Coordinates of the second and third points.

    Returns:
    float: Beta in degrees.
    """
    x2, y2 = firstPoint
    x3, y3 = secondPoint
    return math.degrees(math.atan((x3 - x2) / (y3 - y2)))


import math


def calculate_scale(pixel_point1, pixel_point2, real_point1, real_point2):
    """
    Calculate the scale (pixel/mm) between two points.

    Parameters:
    pixel_point1, pixel_point2: Tuples representing pixel coordinates of the two points (x, y).
    real_point1, real_point2: Tuples representing real-world coordinates of the two points (X, Y) in mm.

    Returns:
    float: Scale in pixels per mm.
    """
    # Unpack the pixel and real-world points
    x1, y1 = pixel_point1
    x2, y2 = pixel_point2
    X1, Y1 = real_point1
    X2, Y2 = real_point2

    # Pixel distance (Euclidean distance)
    pixel_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # Real-world distance (Euclidean distance)
    real_distance = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
    # Scale calculation
    scale = pixel_distance / real_distance
    return scale


import math

def calculate_movement(x2, y2, pixel_per_mm, Alpha_deg, Beta_deg):
    """
    Calculates the amount of X and Y movement in mm to reach the camera axis origin.

    Parameters:
    x2 (float): Value for x2 in pixels.
    y2 (float): Value for y2 in pixels.
    pixel_per_mm (float): Conversion factor from pixels to mm.
    Alpha_deg (float): Angle Alpha in degrees.
    Beta_deg (float): Angle Beta in degrees.

    Returns:
    tuple: (T1, T2) where T1 is the X movement and T2 is the Y movement in mm.
    """
    # Convert angles from degrees to radians
    Alpha = math.radians(Alpha_deg)
    Beta = math.radians(Beta_deg)

    # Calculate t1 and t2
    t1 = x2 * pixel_per_mm
    t2 = y2 * pixel_per_mm

    # Calculate T1 and T2
    T1 = t1 * math.sin(Beta) + t2 * math.sin(Alpha)
    T2 = t1 * math.cos(Beta) + t2 * math.cos(Alpha)

    return T1, T2

# Example usage:
if __name__ == "__main__":
    pass