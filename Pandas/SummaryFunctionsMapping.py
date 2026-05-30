import pandas as pd

reviews = pd.read_csv("C:/Users/Turjo/OneDrive/Desktop/Python/Pandas/input/winemag-data-130k-v2.csv",  index_col = 0)
pd.set_option('display.max_rows', 5)

print(reviews.points.describe())
print(reviews.taster_name.describe())

# to calculate the mean

# mean(): Calculates the average of a numerical column
print(reviews.points.mean())

# unique(): Returns a list of all the distinct values in a column, dropping any duplicates.
print(reviews.taster_name.unique())

# value_counts(): Counts exactly how many times each unique value appears in the column.

print(reviews.taster_name.value_counts())

# Here, taster_name is the column.

# Map -> creating new representation from existing data

review_points_mean = reviews.points.mean()
print(reviews.points.map(lambda p : p - review_points_mean))

# There is also another equivalent method called apply()


# Because of axis='columns', Pandas feeds your DataFrame into this function row-by-row, automatically doing this math for every single review.

def remean_points(row):
    row.points = row.points - review_points_mean
    return row


print(reviews.apply(remean_points, axis= 'columns'))


# just prints the first row
reviews.head(1)


# fastest way to map

review_points_mean = reviews.points.mean()
print(reviews.points - review_points_mean)

# combining information

print(reviews.country + ' - ' + reviews.region_1)

