import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use('bmh')
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["mathtext.rm"] = "Times New Roman"
plt.rcParams["font.size"] = 14

# Check arguments
import sys
args = sys.argv
if len(args) != 2:
    sys.exit()

# Read csv file
# csv = pd.read_csv(args[1], header=None)
csv = pd.read_csv(args[1])

# Convert to numpy array
L_n = csv.values
print(L_n.shape)
print(L_n)

# Get each column
L        = L_n[:,0]
n        = L_n[:,1]
n_over_L = n / L
# print(n_over_L)

# Creat figure
plt.figure(figsize=(9, 5))
plt.xticks([1, 20, 40, 60, 80, 100], fontsize=14)
plt.xlabel('$L$', fontsize=14)

# Number of points
# plt.scatter(L, n, color='black')
# plt.ylabel('Number of points', fontsize=14)

# Number of points in an ensemble
plt.scatter(L, n_over_L, color='black')
plt.yticks([0, 20000, 40000, 60000, 80000, 100000, 120000], fontsize=14)
plt.ylabel('Number of points in an ensemble', fontsize=14)

# plt.grid()
# plt.legend(fontsize=14)
# plt.gca().set_aspect('equal')

plt.show()