# IN: Bx2 matrix wth (r, z)
# RETURN: (r, (0,1), (0,1))
import numpy as np

# INPUT: B-length array with 2-tuple
# OUTPUT:
def ground_line_filtering_proto(input_arr: list) -> list:
    fin: list = []

    for i in range(len(input_arr)):
        if i == len(input_arr) - 1:
            r1: float = input_arr[i - 1][0] if i != 0 else 0
            r2: float = input_arr[i][0]

            z1: float = input_arr[i - 1][1] if i != 0 else 0
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

    return fin




s = 1
input = [(1, 0.1),
         (2, 0.05),
         (3, 0.034),
         (4, 0.1234),
         (5, 0.1232),
         (6, 0.043),
         (7, 0.12),
         (8, 0.012),
         (9, 0.12),
         (10, 0.02343),
         (11, 0.121),
         (12, 0.122),
         (13, 0.12432)]

ret: list = ground_line_filtering_proto(input)
print(f"{len(ret)} : {ret}")
