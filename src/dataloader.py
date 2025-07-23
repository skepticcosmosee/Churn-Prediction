import pandas as pd
data_path='E:/Churn-Prediction-1/data/maindata1.csv'

df=pd.read_csv(data_path)
print(df.shape)
print(df.head)
print(df.info)
print(df.isnull().sum())