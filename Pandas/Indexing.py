import pandas as pd

reviews = pd.read_csv("C:/Users/Turjo/OneDrive/Desktop/Python/Pandas/input/winemag-data-130k-v2.csv",  index_col = 0)
pd.set_option('display.max_rows', 5)
# pd.set_option('display.max_columns', None)

print(reviews.country)
print(reviews['country']) 

# Two ways of selecting specific series

#if we want to access specific value
print(reviews['country'][0])

print(reviews)

# iloc is row first so, this one will select the first row
print(reviews.iloc[0])

# loc and iloc are row-first , column-second!
# like reviews.iloc[row, column] 
# Normally in python data[column][row] - works like this

print(reviews.iloc[:, 0]) # : operator means every row here
print(reviews.iloc[:3, 0]) # It will print three rows -> 0, 1, 2
print(reviews.iloc[1:3, 0]) # selecting the second and third rows
print(reviews.iloc[[0, 1, 2], 0])
print(reviews.iloc[-5:]) # will select the last 5 elements

# label based selection
print(reviews.loc[0, 'country'])
print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])


# iloc -> 0 : 10 will select 0, ....,9
# loc -> 0 : 10 will select 0,......,10


#conditional selection

# ==
print(reviews.country == 'Italy')
# using loc
print(reviews.loc[reviews.country == 'Italy'])
# &
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])
# |
print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])

# isin 
print(reviews.loc[reviews.country.isin(['Italy', 'France'])])

# isnull / notnull
print(reviews.loc[reviews.price.notnull()])


# assigning data

reviews['critic'] = 'everyone'
print(reviews['critic'])