import numpy as np
import pandas as pd
import math

THRESHOLD_M: float = 10
THRESHOLD_M_SMALL: float = 0.05
THRESHOLD_B = 0.2
THRESHOLD_ERROR = 0.1


def ground_line_filtering(input_arr: list) -> list:
    final_output: list = []
    segs: list = []
    points_r: list = []
    points_z: list = []
    np_arr_r: np.array = np.array(points_r)
    np_arr_z: np.array = np.array(points_z)
    counter_list: list = []

    for ind in range(len(input_arr)):
        point: tuple = input_arr[ind]

        if len(points_r) >= 2:
            points_r.append(point[0])
            points_z.append(point[1])
            np_arr_r: np.array = np.array(points_r)
            np_arr_z: np.array = np.array(points_z)

            design_matrix = np.vstack([np_arr_r, np.ones(len(np_arr_r))]).T

            reg_result = np.linalg.lstsq(design_matrix, np_arr_z, rcond=0)
            m, b = reg_result[0]
            rmse: float = np.sqrt(reg_result[1] / len(reg_result[1]))

            if (
                (abs(np.rad2deg(np.arctan(m))) <= THRESHOLD_M)
                and (rmse <= THRESHOLD_ERROR)
                and (len(points_r) != len(input_arr))
            ):
                continue

            np_arr_r = np_arr_r[:-1]
            np_arr_z = np_arr_z[:-1]
            design_matrix = np.vstack([np_arr_r, np.ones(len(np_arr_r))]).T

            m, b = np.linalg.lstsq(design_matrix, np_arr_z, rcond=0)[0]

            segs.append((m, b, np_arr_r[0], np_arr_r[-1]))
            counter_list.append(ind)
            np_arr_r = np.array([])
            np_arr_z = np.array([])
            ind -= 1
        else:
            points_r.append(point[0])
            points_z.append(point[1])
            np_arr_r: np.array = np.array(points_r)
            np_arr_z: np.array = np.array(points_z)

    print(counter_list)

    # ind_seg = 0
    # for ind in range(len(input_arr)):
    #     if ind in counter_list:
    #         ind_seg += 1

    #     fin +=

    for ind, point in enumerate(input_arr):
        if ind == 0:
            final_output.append(
                (point[0], (segs[0][0], segs[0][1]), (segs[0][0], segs[0][1]))
            )
            continue
        elif ind == len(input_arr) - 1:
            final_output.append(
                (point[0], (segs[-1][0], segs[-1][1]), (segs[-1][0], segs[-1][1]))
            )
            continue

        for ind2, seg in enumerate(segs):
            if seg[2] < point[0] and point[0] < seg[3]:
                final_output.append((point[0], (seg[0], seg[1]), (seg[0], seg[1])))
            else:
                if seg[3] == point[0]:
                    nseg = segs[ind2 - 1]
                    final_output.append(
                        (point[0], (nseg[0], nseg[1]), (seg[0], seg[1]))
                    )

    return final_output
