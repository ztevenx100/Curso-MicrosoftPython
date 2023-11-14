#App.py

# statement(s) if test

# test 1
a = 97
b = 55
# test expression
if a < b:
    # statement to be run
    print(b)

print(a)

# test 1
a = 24
b = 44
if a <= 0:
    print(a)
print(b)

# test 2
a = 27
b = 93
if a >= b:
    print(a)
else:
    print(b)

a = 27
b = 93
if a <= b:
    print("a is less than or equal to b")
elif a == b:
    print("a is equal to b")

# test 3
a = 27
b = 93
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else: 
    print ("a is equal to b") 

# test 4
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

# exam 1
object_size = 10
if object_size > 5:
    print('We need to keep an eye on this object')
else:
    print('Object poses no threat.')

# test 5
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

# test 6
a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)

# exam 2
object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')