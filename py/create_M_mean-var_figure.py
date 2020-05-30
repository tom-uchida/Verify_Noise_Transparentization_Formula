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
L       = L_mean_var[:,0]
mean    = L_mean_var[:,1]
var     = L_mean_var[:,2]
M_mean  = L_mean_var[:,3]

# Get the index that meets the conditions
idx = np.where(M_mean<=50)
idx = np.append(idx, np.max(idx)+1)
print(idx)

# Creat figure
plt.figure(figsize=(8, 6))
plt.xlabel('$M$', fontsize=14)
plt.xticks([1, 10, 20, 30, 40, 50], fontsize=14)

# Mean
# plt.scatter(L, mean, color='black')
# plt.yticks([0, 50, 100, 150], fontsize=14)
# plt.ylabel('Mean pixel value', fontsize=14)

# Variance
# plt.scatter(M_mean[idx], var[idx], color='black')
# plt.ylabel('$V_\mathrm{p}$', fontsize=14)
# # plt.ylabel('Variance of pixel values', fontsize=14)
# plt.yticks([0, 500, 1000, 1500], fontsize=14)

# 1/Variance
plt.scatter(M_mean[idx], var[idx]**(-1), color='black')
plt.ylabel('$1 / V_\mathrm{p}$', fontsize=14)
plt.yticks([0, 0.01, 0.02, 0.03, 0.04, 0.05], fontsize=14)

# plt.grid()
# plt.legend(fontsize=14)
# plt.gca().set_aspect('equal')

plt.show()