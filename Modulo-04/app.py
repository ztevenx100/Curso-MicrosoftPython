#app.py

#Used strings and methods

# test 1
fact = "The Moon has no atmosphere."
fact = fact + "No sound can be heard on the Moon."
print(fact)

# test 2
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline2 = """Facts about the Moon:
 There is no atmosphere. 
 There is no sound."""
print(multiline2)

# test 3
heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

# test 4
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)

# test 5
print("Moon" in "This text will describe facts and challenges with space travel")
print("Moon" in "This text will describe facts about the Moon")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))
print(temperatures.find("Mars"))

print(temperatures.count("Moon"))
print(temperatures.count("Mars"))

# test 6
print("The Moon And The Earth".lower())
print("The Moon And The Earth".upper())

# test 7
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

# test 8
print("-60".startswith('-'))

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

# test 9
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)
print("temperatures" in text.lower())


# test 10
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))

#exam 1
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. 
There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. 
This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

#exam 2
sentences = text.split('. ')
print(sentences)

#exam 3
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)

# test 11
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

# test 12
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))

# test 12
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

print(round(100/6, 1))
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)

#exam 3
name = 'Ganymede'
planet = 'Mars'
gravity = '1.45'

#exam 4
template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

#exam 5
print(template.format(name=name, planet=planet, gravity=gravity))



