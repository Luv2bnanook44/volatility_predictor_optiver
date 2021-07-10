import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pyarrow.parquet as pq
import pyarrow as pa

from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error
from sklearn.metrics import median_absolute_error, mean_squared_error, mean_squared_log_error
import statsmodels.tsa.api as smt
import statsmodels.api as sm

class volatility_pipeline():
    
    def __init__(self):
        
        self.data = None
    
    def fit(self, df, amount=100000):
        '''data must be csv file; pipeline for data'''
        
        num_sections = len(df) // amount
        section = np.random.choice(range(1, num_sections))
        start = section+amount
        end = section+(2*amount)
        self.data = df.iloc[start:end]
        
        
        
        