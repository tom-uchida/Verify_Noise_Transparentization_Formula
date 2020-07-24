import numpy as np
import pandas as pd

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

# Calc. r2_score
from sklearn.metrics import r2_score
alpha = 0.5
y_true = M_mean
y_pred = M = alpha * L
print("\nr2_score:", round(r2_score(y_true, y_pred),2) )

# >>> from sklearn.metrics import r2_score
# >>> y_true = [3, -0.5, 2, 7]
# >>> y_pred = [2.5, 0.0, 2, 8]
# >>> r2_score(y_true, y_pred)
# 0.948...