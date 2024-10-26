import numpy as np
import matplotlib.pyplot as plt


def classify_points(
    points: list[list[float]],
    bins: list[int],
    lines: list[tuple],
    threshold: float,
    bin_ranges: list,
) -> list[list[float]]:
    res = np.empty((0, 2))

    plt.plot(points[:, 0], points[:, 1], "o", label="original data")
    for x in bin_ranges:
        plt.axvline(x=x, color="g", linestyle="--")
    for idx in range(len(lines)):

        baskmask = bins == idx
        bin_points = points[baskmask]
        r, (m1, b1), (m2, b2) = lines[idx]
        lasky = bin_points[:, 0] <= r
        left = bin_points[lasky]
        rasky = bin_points[:, 0] > r
        right = bin_points[rasky]
        lomparey = m1 * left[:, 0] + b1
        romparey = m2 * right[:, 0] + b2

        # Plotting without threshold
        if idx < len(lines) - 1:
            LL = np.arange(bin_ranges[idx], r, 0.01)
            RR = np.arange(r, bin_ranges[idx + 1], 0.01)
            plt.plot(LL, b1 + m1 * LL, "r")
            plt.plot(RR, b2 + m2 * RR, "b")

            # Plotting with threshold
            plt.plot(LL, b1 + m1 * LL + threshold, "r--")
            plt.plot(RR, b2 + m2 * RR + threshold, "b--")

        leheasky = (lomparey + threshold) < left[:, 1]
        reheasky = (romparey + threshold) < right[:, 1]
        res = np.concatenate((res, np.concatenate((left[leheasky], right[reheasky]))))

    plt.show()

    return res
