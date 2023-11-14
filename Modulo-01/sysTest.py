# sysTest
import sys

#Used system tools or at run time

# test 1
#comand py sysTest.py 2023-01-01
print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg

# test 2
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

# test 3
print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
#Concatenate String
print(first_number + second_number)
#Sum ints
print(int(first_number) + int(second_number))

# test 4
parsecs_input = input("Input number of parsecs:")
lightyears = 3.26156 * int(parsecs_input)

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")


