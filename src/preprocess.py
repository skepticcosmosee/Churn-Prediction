import pandas as pd
from sklearn.model_selection import train_test_split
from dataloader import df

cat_cols=df.select_dtypes(include=['object']).columns.tolist()
cat_cols.remove('Churn')

num_cols=df.select_dtypes(include=['int64','float32']).columns.tolist()

print(cat_cols)
print(num_cols)

df.Churn=df['Churn'].map({'Yes':1,'No':0})

df=pd.get_dummies(df,columns=cat_cols,drop_first=True)

X=df.drop('Churn',axis=1)
Y=df['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)

