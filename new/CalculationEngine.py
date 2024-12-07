import inspect
import math
from icecream import ic


def icAll(func, verbose=True):
    """
    A decorator that uses icecream to automatically applies ic to every variable in the function

    :param func: Function to be decorated
    :param verbose: If True, print meta information ('variables', 'func', 'signature', 'parameters')
    :return: decorator
    """
    def wrapper(*args, **kwargs):
        # Retrieve the function's signature (parameters)
        signature = inspect.signature(func)
        parameters = signature.parameters

        # Combine function arguments and keyword arguments into a dictionary
        variables = {k: v for k, v in zip(parameters, args)}
        variables.update(kwargs)

        # Retrieve local variables defined in the function body
        result = func(*args, **kwargs)

        # Get the local variables in the function using inspect
        frame = inspect.currentframe().f_locals
        variables.update(frame)

        # Log variables using icecream
        for var_name, var_value in variables.items():
            if verbose:
                ic(var_name, var_value)  # Print variable names and values if verbose is Truei
            else:
                if var_name not in ['variables', 'func', 'signature', 'parameters']:
                    ic(var_name, var_value)

        return result

    return wrapper


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


def calculate_scale(cameraPoint1, cameraPoint2, real_point1, real_point2):
    """
    Calculate the scale (pixel/mm) between two points.

    Parameters:
    pixel_point1, pixel_point2: Tuples representing pixel coordinates of the two points (x, y).
    real_point1, real_point2: Tuples representing real-world coordinates of the two points (X, Y) in mm.

    Returns:
    float: Scale in pixels per mm.
    """
    # Unpack the pixel and real-world points
    x1, y1 = cameraPoint1
    x2, y2 = cameraPoint2
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

# @icAll
def calculateCameraMovementOffset(cameraPoint1, real_point1, real_point2, cameraPoint2=None, cameraPoint3=None):
    # ic(cameraPoint1, cameraPoint2, cameraPoint3, real_point1, real_point2)
    cameraPoint2, cameraPoint3 = extrapolateManipulatorPosition(
        cameraPoint1, cameraPoint2
    ) if cameraPoint3 is None else (cameraPoint2, cameraPoint3)

    alpha = calculate_alpha(cameraPoint1, cameraPoint2)
    beta = calculate_beta(cameraPoint2, cameraPoint3)
    scalePixelInMilimeter = calculate_scale(cameraPoint1, cameraPoint2, real_point1, real_point2)
    ic(alpha, beta, scalePixelInMilimeter)
    cameraXOffset, cameraYOffset = calculate_movement(cameraPoint2[0], cameraPoint2[1], scalePixelInMilimeter, alpha, beta)

    return cameraXOffset, cameraYOffset

def extrapolateManipulatorPosition(firstPoint, secondPoint=None, defaultInitialOffset = 2.0):
    x1, y1 = firstPoint
    secondPoint = (x1 + defaultInitialOffset, y1 - defaultInitialOffset) if secondPoint is None else secondPoint
    x2, y2 = secondPoint
    # Calculate thirdPoint by rotating firstPoint around secondPoint by +90 degrees
    x3 = x2 + (y1 - y2)
    y3 = y2 - (x1 - x2)

    thirdPoint = (x3, y3)

    return secondPoint, thirdPoint



# Example usage:
if __name__ == "__main__":
    campoint1 = (1, 3)
    realpoint1 = (2, 4)
    campoint2 = (1.5, 1.5)
    realpoint2 = (2, 2.5)
    campoint3 = (3, 2)
    # ic(calculate_alpha(campoint1, campoint2))
    # ic(calculate_beta(campoint2, campoint3))
    # ic(calculate_scale(campoint1, campoint2, realpoint1, realpoint2))
    # ic(calculate_movement(campoint2[0], campoint2[1], calculate_scale(campoint1, campoint2, realpoint1, realpoint2),
    #                          calculate_alpha(campoint1, campoint2), calculate_beta(campoint2, campoint3)))

    # ic(calculateCameraMovementOffset(campoint1, campoint2, campoint1, realpoint1, realpoint2))

    firstPoint = (1, 3)
    secondPoint = (3, 1)
    thirdPoint = (5,3)
    # ic(extrapolateManipulatorPosition(firstPoint))
    ic(calculateCameraMovementOffset(campoint1, realpoint1, realpoint2))
    ic(calculateCameraMovementOffset(campoint1, realpoint1, realpoint2, cameraPoint2=secondPoint, cameraPoint3=thirdPoint))
