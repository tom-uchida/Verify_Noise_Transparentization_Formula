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
csv = csv.values
print(csv.shape)
print(csv)

# Get each column
L       = csv[:,0]
M_mean  = csv[:,1]
M_max   = csv[:,2]
M_min   = csv[:,3]
M_std   = csv[:,4]

# Draw a linear function(Theoretical linear function)
alpha = 0.5
L_R = np.arange(1, 100, 1)
M = alpha * L_R
plt.plot(L_R, M, "--", color='red', label=r"$M= \alpha L (\alpha=0.5)$")

# M
# plt.scatter(L, M_max, color='black', label=r"$M_\mathrm{max}$", marker="^")
# plt.scatter(L, M_mean, color='black', label=r"$M_\mathrm{mean}$", marker="o")
# plt.scatter(L, M_min, color='black', label=r"$M_\mathrm{min}$", marker="v")

# Draw error bar
plt.errorbar(L, M_mean, M_std, fmt='ok', elinewidth=1, capsize=3, ecolor='black')

# plt.grid()
plt.legend(fontsize=14)
# plt.gca().set_aspect('equal')

plt.xticks([1, 20, 40, 60, 80, 100], fontsize=14)
plt.xlabel('$L$', fontsize=14)
plt.yticks([0, 20, 40, 60, 80, 100], fontsize=14)
plt.ylabel('$M$', fontsize=14)

plt.show()