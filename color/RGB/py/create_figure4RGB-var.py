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
L_var = csv.values
print(L_var.shape)
print(L_var)

# Get each column
L      = L_var[:,0]
var_R  = L_var[:,1]
var_G  = L_var[:,2]
var_B  = L_var[:,3]

# Creat figure
plt.xticks([1, 20, 40, 60, 80, 100], fontsize=14)
plt.xlabel('$L$', fontsize=14)

# Var
# plt.scatter(L, var_R, color='red')
# plt.scatter(L, var_G, color='green')
# plt.scatter(L, var_B, color='blue')
# plt.yticks([0, 1000, 2000, 3000, 4000, 5000, 6000], fontsize=14)
# plt.ylabel('$\mathrm{Variance}$', fontsize=14)

# Inverse Var
plt.scatter(L, 1/var_R, color='red')
plt.scatter(L, 1/var_G, color='green')
plt.scatter(L, 1/var_B, color='blue')
plt.yticks([0, 0.01, 0.02, 0.03, 0.04, 0.05], fontsize=14)
plt.ylabel('$1/\mathrm{Variance}$', fontsize=14)

# plt.grid()
# plt.legend(fontsize=14)
# plt.gca().set_aspect('equal')

plt.show()