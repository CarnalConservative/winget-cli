from numpy import median
import pandas

census_data = pandas.read_csv("census.csv",header= None)

age = census_data[0].median()


print(census_data[0])
print(age)