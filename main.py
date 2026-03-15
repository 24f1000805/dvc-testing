import numpy as np
import pandas as pd
train = pd.read_csv("/Users/bhojender/Desktop/IITM/ml-project/DVC/train.csv")
print(train.isnull().sum())
print(train.columns)
train['post_id_edition'] = train['post_id']+10
print(train.columns)