import numpy as np
import pandas as pd
import math

THRESHOLD_M: float = 0.1
THRESHOLD_M_SMALL: float = 0.05
THRESHOLD_B = 0.2
THRESHOLD_ERROR = 0.1


def ground_line_filtering(input_arr: list) -> list:
    fin: list = []
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

            segs.append((m, b))
            counter_list.append(ind)
            np_arr_r = np.array([])
            np_arr_z = np.array([])
            ind -= 1
        else:
            points_r.append(point[0])
            points_z.append(point[1])
            np_arr_r: np.array = np.array(points_r)
            np_arr_z: np.array = np.array(points_z)

        """    
        if i == len(input_arr) - 1:
            r2: float = input_arr[i][0]

            z2: float = input_arr[i][1]

            s1: float = (z2 - z1) / (r2 - r1)
            inter1: float = z2 - r2 * s1

            fin.append((r2, (s1, inter1), (s1, inter1)))
            continue

        r1: float = input_arr[i - 1][0] if i != 0 else 0
        r2: float = input_arr[i][0]
        r3: float = input_arr[i + 1][0]

        z1: float = input_arr[i - 1][1] if i != 0 else 0
        z2: float = input_arr[i][1]
        z3: float = input_arr[i + 1][1]

        s1: float = (z2 - z1) / (r2 - r1)
        s2: float = (z3 - z2) / (r3 - r2)

        inter1: float = z2 - r2 * s1
        inter2: float = z2 - r2 * s2

        fin.append((r2, (s1, inter1), (s2, inter2)))
        """

    return segs
