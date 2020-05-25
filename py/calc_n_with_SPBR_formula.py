import sys
import numpy as np

args = sys.argv

alpha = 0.649083
s = 0.1
S = 1.0
L = int(args[1])

# alpha = 1 - pow(1 - (s/S), (n/L))
n = np.log(1 - alpha) / np.log(1 - s/S) * L
print("n: ", n)