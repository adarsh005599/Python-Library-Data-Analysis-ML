import pandas as pd

data = {
    'name' : ['adarsh', 'abhinav', 'raushan', 'shreya'],
    'age' : [20,23,24,21],
    'city' : ['delhi', 'kashi', 'Noida', 'kolkata'],
    'Skills' : ['ML', 'AI', 'backend', 'BlockChain']
}

df = pd.DataFrame(data)
print(df)

# df.to_csv('new01.csv', index=False) # as csv
df.to_numpy('newExl.') 