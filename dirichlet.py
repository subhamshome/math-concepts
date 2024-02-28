# Plot of Prime Numbers and Dirichlet's Theorem

import numpy as np
import matplotlib.pyplot as plt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def polar_plot(n, prime):
    for i in range(1, n):
        if prime:
            if is_prime(i):
                plt.polar(i, i, "o", color="blue", markersize=2)

                plt.axis("off")
        else:
            plt.polar(i, i, "o", color="blue", markersize=2)

            plt.axis("off")
    plt.show()


polar_plot(100000, True)
