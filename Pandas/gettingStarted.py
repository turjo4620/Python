import pandas as pd

pd.DataFrame({
    'Turjo' : ['CSE', 'Secton C'],
    'Prince' : ['CSE' , 'Secton C']},
    index= ['Dept.', 'Section']                                    
)

pd.Series([1, 2, 3, 4, 5])
pd.Series([30, 40, 50],
        index=['2015 sales', '2016 sales', '2017 sales'], name ='Product A')

# Dataframe is just a bunch of Series "glued together".

#working with csv file -> commands 
#                           ->pd.read_csv(file path)
#                           ->pd.shape() -> returns (records, columns)
#                           ->pd.head() -> works with the 5 rows
                        