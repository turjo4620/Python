import pandas as pd
pd.set_option('display.max_rows', 5)


# default indexing

check = pd.DataFrame({'Apples' : [30],
              'Bananas' : [21],
              })
print(check)

#    Apples  Bananas
# 0      30       21

fruit_sales = pd.DataFrame({
    'Apples' : [35, 41],
    'Bananas' : [21, 34]},
    index=['2017 Sales', '2018 Sales']
    )
print(fruit_sales)

# Manual indexing
#             Apple  Bananas
# 2017 Sales     35       21
# 2018 Sales     41       34

ingredients = pd.Series([
    '4 cups', '1 cup', '2 large', '1 can'],
    index=['Flour', 'Milk', 'Eggs', 'Spam'], name = 'Dinner')
print(ingredients)

# Flour     4 cups
# Milk       1 cup
# Eggs     2 large
# Spam       1 can
# Name: Dinner, dtype: str


# if we want to save a datafram to csv file

animals = pd.DataFrame({
    'Cows' : [12, 20],
    'Goats' : [22, 19]},
    index= ['Year 1', 'Year 2'])
animals.to_csv("cows_and_goats.csv")
