#app.py
from math import ceil, floor

#Use mathematical operators

#test 1
answer = 30 + 12
print(answer)

#test 2
difference = 30 - 12
print(difference)

#test 3
product = 30 * 12
print(product)

#test 4
quotient = 30 / 12
print(quotient)

#test 5
seconds = 1042
display_minutes = seconds // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

#test 6
result_1 = 1032 + 26 * 2
print(result_1)

result_2 = 1032 + (26 * 2)
print(result_2)

#exam 1
first_planet = 149597870
second_planet = 778547200

distance_km = second_planet - first_planet
print(distance_km)
distance_mi = distance_km / 1.609344
print(distance_mi)

#test 7
demo_int = int('215')
print(demo_int)
demo_float = float('215.3')
print(demo_float)

#test 8
print(39 - 16)
print(16 - 39)
print(abs(39 - 16))
print(abs(16 - 39))

#test 9
print(round(14.5))

#test 10
round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

#exam 2
first_planet_input = input('Enter the distance from the sun for the first planet in km')
second_planet_input = input('Enter the distance from the sun for the second planet in km')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = second_planet - first_planet
print(abs(distance_km))


