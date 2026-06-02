matrix = [[1, 2 , 3],
          ['a', 'b', 'c']]
print(matrix)

print(matrix[-1]) # printing the last row 
print(matrix[0][0]) # first item
print(matrix[-1][-1]) # last item


# slicing

matrix = [
    ['a' , 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
print(matrix[ : 2]) # first two row 
print(matrix[1 :]) # last two row

# if we want to get g and h
print(matrix[2][ : 2]) # ['g', 'h']
