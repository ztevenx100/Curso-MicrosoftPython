# program.py
from datetime import date

#Used types

# test 1
sum = 1 + 2 # 3
product = sum * 2
print("Product result: " + str(product))

# test 2
left_side = 10
right_side = 5
print (left_side / right_side) # 2
print (type(left_side / right_side) )

# test 3
print(date.today())

# test 4
print("Today's date is: " + str(date.today()))

# test 5
parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

