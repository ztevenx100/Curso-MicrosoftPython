#App.py

# use data dictionary

#test 1
name = 'Earth'
moons = 1

earth_name = 'Earth'
earth_moons = 1

jupiter_name = 'Jupiter'
jupiter_moons = 79

planet = {
    'name': 'Earth',
    'moons': 1
}
print(planet.get('name'))
# planet['name'] is identical to using planet.get('name')
print(planet['name'])

#test 2
wibble = planet.get('wibble') # Returns None
#wibble = planet['wibble'] # Throws KeyError

#test 3
planet.update({'name': 'Makemake'})
# No output: name is now set to Makemake.
planet['name'] = 'Makemake'
# No output: name is now set to Makemake.
print(planet['name'])

#test 4
planet.update({
    'name': 'Jupiter',
    'moons': 79
})
planet['name'] = 'Jupiter'
planet['moons'] = 79

#test 5
planet['orbital period'] = 4333
# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }
print(planet)

planet.pop('orbital period')
# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }
print(planet)

#test 5
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }
print(planet)
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

#exam 1
planet = {
    'name': 'Mars',
    'moons': 2
}
print(f'{planet["name"]} has {planet["moons"]} moon(s)')

planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

#test 6
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

#test 7
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# Because december exists, the value will be 3.1

#test 8
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter.')

#exam 2
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons = planet_moons.values()
total_planets = len(planet_moons.keys())

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet has an average of {average} moons')