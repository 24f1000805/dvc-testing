import numpy as np
import pandas as pd
train = pd.read_csv("/Users/bhojender/Desktop/IITM/ml-project/DVC/train.csv")
print(train.isnull().sum())