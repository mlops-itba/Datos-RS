# %%
import pandas as pod
import numpy as np
import mlflow
# %%
mlflow.set_experiment(EDA)
mlflow.log_metric("prueba", 3)
mlflow.end_run()
# %%
