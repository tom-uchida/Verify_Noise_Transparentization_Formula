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
# plt.figure(figsize=(8, 4))
plt.xticks([1, 20, 40, 60, 80, 100], fontsize=14)
plt.xlabel('$L$', fontsize=14)

# Mean
# plt.scatter(L, mean, color='black')
# plt.hlines(0.9, 1, 100, "red", linestyles='dashed')
# plt.text(1, 0.8, r"$r_\mathrm{theorical} = 0.9$", color='red', fontsize='14')
# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=14)
# plt.ylabel(r'$r_{\mathrm{G/R}}$', fontsize=14)

# Variance
# plt.scatter(L, var, color='black')
# plt.ylabel('$\mathrm{Variance}$', fontsize=14)
plt.scatter(L, var**(-1), color='black')
plt.ylabel('$1 / \mathrm{Variance}$', fontsize=14)
plt.yticks([0, 100, 200, 300, 400, 500], fontsize=14)


# plt.grid()
# plt.legend(fontsize=14)
# plt.gca().set_aspect('equal')

plt.show()