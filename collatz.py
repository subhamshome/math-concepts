# Collatz Conjecture

import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--value", type=int, help="An integer value")
args = parser.parse_args()

value = int(args.value)
collatz_list = []

while value > 1:
    if value % 2 == 0:
        value = value / 2
    else:
        value = 3 * value + 1
    print(int(value))

    collatz_list.append(int(value))


print(collatz_list)

x = np.arange(len(collatz_list))
plt.plot(collatz_list)
plt.scatter(x, collatz_list)
plt.xlabel("Iteration")
plt.ylabel("Value")
plt.title("Collatz List")
plt.show()
