from SegmentGenerator import ground_line_filtering
from BinClassifier import bin_classifier
import numpy as np

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
