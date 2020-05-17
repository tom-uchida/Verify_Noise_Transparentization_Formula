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
L_mean_max = csv.values
print(L_mean_max.shape)
print(L_mean_max)

# Get each column
L       = L_mean_max[:,0]
M_mean  = L_mean_max[:,1]
M_max   = L_mean_max[:,2]

# Creat figure
# plt.figure(figsize=(8, 4))
plt.xticks([1, 20, 40, 60, 80, 100], fontsize=14)
plt.xlabel('$L$', fontsize=14)

# Mean
plt.scatter(L, M_mean, color='black', marker="")
plt.scatter(L, M_max, color='red')
plt.xticks([0, 20, 40, 60, 80, 100], fontsize=14)
plt.yticks([0, 20, 40, 60, 80, 100], fontsize=14)
plt.ylabel('$M$', fontsize=14)

# plt.grid()
# plt.legend(fontsize=14)
# plt.gca().set_aspect('equal')

plt.show()