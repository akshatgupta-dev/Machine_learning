import pandas as pd

data = pd.read_csv('Housing_price_work/housing.csv') 


print(data.info)
print(data.head())

data.dropna(inplace=True)
ocean_data = pd.get_dummies(data.ocean_proximity)
data = data.join(ocean_data).drop('ocean_proximity', axis=1)