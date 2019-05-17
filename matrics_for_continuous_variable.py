from sklearn import metrics
import numpy as np
y_true = [3, 0.0, 2, 7]
y_pred = [2.5, -0.3, 2, 8]
metrics.mean_absolute_error(y_true, y_pred) # MAE
metrics.mean_absolute_error(y_true, y_pred) * 100 # MAPE
metrics.mean_squared_error(y_true, y_pred) # MSE
metrics.mean_squared_error(y_true, y_pred) ** 0.5 # RMSE
np.sqrt(metrics.mean_squared_error(y_true, y_pred)) # RMSE
