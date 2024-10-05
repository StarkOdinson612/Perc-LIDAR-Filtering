import numpy as np
import pandas as pd

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

    for ind, point in enumerate(len(input_arr)):
        if len(points_r) >= 2:
            np.append(np_arr_r, point[0])
            np.append(np_arr_z, point[1])

            design_matrix = np.vstack([np_arr_r, np.ones(len(np_arr_r))]).T

            reg_result = np.linalg.lstsq(design_matrix, np_arr_z, rcond=0)
            m,b = reg_result[0]
            residuals
            
            if (abs(m) <= THRESHOLD_M) and (m > THRESHOLD_M_SMALL or abs(b) <= THRESHOLD_B) and 

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

    return fin
