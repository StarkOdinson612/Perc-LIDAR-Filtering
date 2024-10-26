import random as rand
import math
import time
import numpy as np


def bin_classifier(Array2d: list[list[float]]) -> list[tuple[float]]:

    start_time = time.time()

    # create vars
    Rmax = 28.3
    Rmin = min([point[0] for point in Array2d])
    B = 3
    Bins_min = [[-1, -1] for _ in range(3)]
    minZ = min(Array2d, key=lambda point: point[2])

    # split Array2d into bins
    for p in Array2d:
        r_val = math.sqrt((p[0] ** 2 + p[1] ** 2))
        bin_num = math.floor(B * (r_val / (Rmax + 0.00001)))
        if Bins_min[bin_num][0] > 0:
            if Bins_min[bin_num][1] > p[2]:
                Bins_min[bin_num][0] = r_val
                Bins_min[bin_num][1] = p[2]
        else:
            Bins_min[bin_num][0] = r_val
            Bins_min[bin_num][1] = p[2]

    end_time = time.time()
    elapsed_time = end_time - start_time  # Calculate the time difference

    ret: list[tuple[float]] = [(bin[0], bin[1]) for bin in Bins_min]

    return ret


def bin_point_classifier(points: list[list[float]], num_bins: int):
    ranges = np.sqrt(points[:, 0] ** 2 + points[:, 1] ** 2)
    pts = []

    for i in range(len(ranges)):
        pts.append((ranges[i], points[i][2]))

    # print("ranges")
    # print(ranges)

    # Calculate range for each point
    # print(segments)
    # import pdb; pdb.set_trace()
    rmax = np.max(ranges)
    rmin = np.min(ranges)
    bin_size = (rmax - rmin) / num_bins
    rbins = np.arange(rmin, rmax, bin_size)

    regments = np.digitize(ranges, rbins) - 1

    np.append(rbins, rmax)

    return (rbins, pts, regments)
