import math
import numpy as np

PI = math.pi


def split_segments(points: list[list[float]], alpha: int) -> list[list[float]]:

    # import pdb; pdb.set_trace()
    angles = np.arctan2(points[:, 1], points[:, 0])  # Calculate angle for each point
    adojangles = np.where(angles < 0, angles + 2 * np.pi, angles)
    sepangles = np.arange(np.min(adojangles), np.max(adojangles), alpha)
    angle_segs = np.digitize(angles, sepangles) - 1  # Map angles to segments

    # for idx in range(len(sepangles)):
    #     seg = angle_segs == idx
    #     seggy = points[seg]
    #     # vis.update_visualizer_window(None, seggy)

    return angle_segs
