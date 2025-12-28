import numpy as np 
import pandas as pd

# making the data
data={
    'name': ['Abhi', 'aditya', 'Neha', 'sweta', 'modi'],
    'Age' : [22 , 21 , 34 , None , None],
    'salary' : [430000 , 340000 , 650000, None , 900000]
}

df = pd.DataFrame(data)
print('Actual data: ', df)

print(df.isnull().sum())

df_drop = df.dropna()
print("after the empty col drop: \n" ,df_drop)

df['Age'].fillna(df['Age'].mean() , inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)
print(df)