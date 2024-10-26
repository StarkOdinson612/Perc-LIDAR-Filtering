import random as rand
import math
import time


def bin_classifier(Array2d: list[list[float]]) -> list[tuple[float]]:
    # create segment randomly
    Array2d = []
    l = 20
    for i in range(300000):
        Array2d.append([rand.random() * l, rand.random() * l, rand.random() * l])

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

    print(ret)

    return ret
