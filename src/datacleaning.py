import pandas as pd
import numpy as np
from dataloader import df

df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')
df=df.dropna(subset=['TotalCharges'])
df.reset_index(drop=True,inplace=True)
df.to_csv("data/cleaned_data",index=False)

