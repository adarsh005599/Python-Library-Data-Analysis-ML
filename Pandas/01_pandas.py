import pandas as pd 

# Adding the new column and rows 

data = {
    'name' : ['adarsh', 'abhinav', 'raushan', 'shreya'],
    'age' : [20,23,24,21],
    'city' : ['delhi', 'kashi', 'Noida', 'kolkata'],
}

data = pd.DataFrame(data)

# data['salary'] = [65000, 75000, 50000,70000]
# print(data)

# using the insert method at specific location
# data.insert(location, 'column add', your_new_data)

# data.insert(3,'hight',[6.0, 5.9, 5.8, 5.2])
# print(data)

# updating the perticular specific data using .loc

data.loc[2, 'age'] = 40
print(data)


