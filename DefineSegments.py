import math
import math.pi as PI


def split_segments(points: list[list[float]], num_seg: int) -> list[list[float]]:

    theta: float = math.radians(200) / num_seg

    segments: list[list[float]] = [[] for _ in range(num_seg)]

    for point in points:
        angle: float = math.atan(point[0], point[1]) + PI / 2
        index: int = angle // theta
