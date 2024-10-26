from SegmentGenerator import ground_line_filtering
from BinClassifier import bin_classifier, bin_point_classifier
from DefineSegments import split_segments
from ClassifyPoints import classify_points
import numpy as np
import math
import random as rand

if __name__ == "__main__":
    # input = [
    #     (1, 0.1),
    #     (2, 0.05),
    #     (3, 0.034),
    #     (4, 0.1234),
    #     (5, 0.1232),
    #     (6, 0.043),
    #     (7, 0.12),
    #     (8, 0.012),
    #     (9, 0.12),
    #     (10, 0.02343),
    #     (11, 0.121),
    #     (12, 0.122),
    #     (13, 0.12432),
    # ]

    points = []
    NUM_BINS: int = 3
    l = 20
    for i in range(300000):
        points.append([rand.random() * l, rand.random() * l, rand.random() * l])

    NUM_SEG: int = 10

    npp: np.array = np.asarray(points)

    segments: list[int] = split_segments(npp, math.pi * 2 / NUM_SEG)

    # for i in range(NUM_SEG):
    #     this_bin: list[list[float]] = []

    fin_points: list[list[float]] = []

    for idx in range(NUM_SEG):
        seg = segments == idx
        this_segment = npp[seg]

        if len(this_segment) == 0:
            continue

        # this_bin: list[tuple[float]] = bin_classifier(segments)
        bin_pts, bin_indices = bin_point_classifier(this_segment, NUM_BINS)

        bin_bits = []

        for idxx in range(NUM_BINS):
            bin_indices = np.asarray(bin_indices)
            bin_pts = np.asarray(bin_pts)
            yy = bin_indices == idxx
            tbins = bin_pts[yy]

            min_z = 1000000
            min_pt: list = []

            for pt in tbins:
                if pt[1] < min_z:
                    min_pt = pt

            bin_bits += [min_pt]

        # print(bin_bits)
        line_segs = ground_line_filtering(bin_bits)

        fin_points += [classify_points(bin_pts, bin_indices, line_segs, 0.1)]

    print(fin_points)

    # ret: list = SegmentGenerator.ground_line_filtering(input)

    # ret = [
    #     (
    #         round(float(i[0]), 1),
    #         (round(float(i[1][0]), 3), round(float(i[1][1]), 3)),
    #         (round(float(i[2][0]), 3), round(float(i[2][1]), 3)),
    #     )
    #     for i in ret
    # ]

    # print(ret)
