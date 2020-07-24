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

# Calculate RMSE
def calc_RMSE(y_true, y_pred):
    mse = np.power(y_true - y_pred, 2).mean()
    return np.sqrt(mse)

alpha = 0.5
y_true = M_mean
y_pred = M = alpha * L
rmse = calc_RMSE(y_true, y_pred)
print(f'RMSE: {round(rmse, 2)}')