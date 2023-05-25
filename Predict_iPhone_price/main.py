import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# part-1, show record
data = pandas.read_csv('iphone_price.csv')
# print(data.head())
plt.scatter(data['version'], data['price']) #not_working
plt.show() #not_working

# part-2, predict result
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[30]]))
