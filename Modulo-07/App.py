# app.py
from time import sleep

# Used for and while

#test 1
user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done')

#test 2
# Create the variable for user input
user_input2 = ''
# Create the list to store the values
inputs = []

# The while loop
while user_input2.lower() != 'done':
    # Check if there's a value in user_input
    if user_input2:
        # Store the value in the list
        inputs.append(user_input2)
    # Prompt for a new value
    user_input2 = input('Enter a new value, or done when done')

#exam 1
new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done')

print(planets)

#test 3
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is ", planets[0])
print("The second planet is ", planets[1])
print("The third planet is ", planets[2])

#test 4
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")

#test 5
countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")

#test 6
new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet or done if done')

for planet in planets:
    print(planet)