#App.py

from datetime import timedelta, datetime

# use and create functions

#test 1
def rocket_parts():
    print("payload, propellant, structure")

rocket_parts()

output = rocket_parts()
output

#test 2
def rocket_parts():
    return "payload, propellant, structure"
output = rocket_parts()
output

#test 3
any([True, False, False])

#test 3
str()
str(15)
print(str(15))

#test 4
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

print(distance_from_earth("Moon"))
print(distance_from_earth("Saturn"))

#test 5
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))

#test 6
print( round(days_to_complete(238855, 75)) )

#exam 1
def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)

print(generate_report(80, 70, 75))


#test 7
def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())
print(arrival_time(hours=0))

#test 8
from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print( arrival_time("Moon") )
print( arrival_time("Orbit", hours=0.13) )

#test 9
def variable_length(*args):
    print(args)

variable_length()
variable_length("one", "two")
variable_length(None)

#test 10
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

print( sequence_time(4, 14, 18) )
print( sequence_time(4, 14, 48) )

#test 11
def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

#exam 2
def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main=50, external=100, emergency=60)
