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
L_mean = csv.values
print(L_mean.shape)
print(L_mean)

# Get each column
L       = L_mean[:,0]
mean_R  = L_mean[:,1]
mean_G  = L_mean[:,2]
mean_B  = L_mean[:,3]

# Creat figure
plt.xticks([1, 20, 40, 60, 80, 100], fontsize=14)
plt.xlabel('$L$', fontsize=14)

# Mean
plt.scatter(L, mean_R, color='red')
plt.scatter(L, mean_G, color='green')
plt.scatter(L, mean_B, color='blue')

plt.hlines(165, 1, 100, "red", linestyles='dashed')
plt.text(1, 170, r"$R_\mathrm{theorical} = 165$", color='red', fontsize='14')
plt.hlines(194, 1, 100, "green", linestyles='dashed')
plt.text(1, 200, r"$G_\mathrm{theorical} = 194$", color='green', fontsize='14')
plt.hlines(149, 1, 100, "blue", linestyles='dashed')
plt.text(1, 130, r"$B_\mathrm{theorical} = 149$", color='blue', fontsize='14')

plt.yticks([0, 50, 100, 150, 200, 250], fontsize=14)
plt.ylabel('$\mathrm{Mean}$', fontsize=14)

# plt.grid()
# plt.legend(fontsize=14)
# plt.gca().set_aspect('equal')

plt.show()