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
L_mean_var = csv.values
print(L_mean_var.shape)
print(L_mean_var)

# Get each column
L    = L_mean_var[:,0]
mean = L_mean_var[:,1]
var  = L_mean_var[:,2]

# Creat figure
plt.figure(figsize=(8, 6))
plt.xticks([1, 20, 40, 60, 80, 100], fontsize=14)
plt.xlabel('$L$', fontsize=14)

# Mean
# plt.scatter(L, mean, color='black')
# plt.hlines(0.9, 1, 100, "red", linestyles='dashed')
# plt.text(1, 0.8, r"$r_\mathrm{theorical} = 0.9$", color='red', fontsize='16')
# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=14)
# plt.ylabel(r'Mean of $r_\mathrm{G/R}$ and $r_\mathrm{B/R}$', fontsize=14)

# Variance
# plt.scatter(L, var, color='black')
# plt.ylabel('$V_\mathrm{p}$', fontsize=14)
# plt.ylabel('$V_\mathrm{ratio}$', fontsize=14)
# # plt.ylabel('Variance of pixel values', fontsize=14)
# plt.yticks([0, 500, 1000, 1500, 2000], fontsize=14)
# plt.yticks([0, 1000, 2000, 3000, 4000, 5000], fontsize=14)

# 1/Variance
plt.scatter(L, var**(-1), color='black')
# plt.ylabel('$1 / V_\mathrm{p}$', fontsize=14)
# plt.ylabel('$1 / V_\mathrm{ratio}$', fontsize=14)
plt.yticks([0, 0.01, 0.02, 0.03, 0.04, 0.05], fontsize=14)
# plt.yticks([0, 0.002, 0.004, 0.006, 0.008, 0.01], fontsize=14)
# # plt.yticks([0, 100, 200, 300, 400, 500], fontsize=14)

# plt.grid()
# plt.legend(fontsize=14)
# plt.gca().set_aspect('equal')

plt.show()