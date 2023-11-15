#App.py

# use error control

#test 1
def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    # main()
    print("error")

#test 2
try:
     open('config2.txt')
except FileNotFoundError:
     print("Couldn't find the config2.txt file!")

#test 3
def main():
    try:
        configuration = open('config2.txt')
    except FileNotFoundError:
        print("Couldn't find the config2.txt file!")

if __name__ == '__main__':
    main()

#test 4
def main1():
    try:
        configuration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!")

def main2():
    try:
        print("try")
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")

def main3():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

#test 5
try:
    open("mars.jpg")
except FileNotFoundError as err:
    print("Got a problem trying to read the file:", err)

try:
    open("config3.txt")
except OSError as err:
     if err.errno == 2:
         print("Couldn't find the config3.txt file!")
     elif err.errno == 13:
        print("Found config.txt but couldn't read it")

#exam 1
loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

parsed_config = {}
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
        parsed_config[key] = value
    except ValueError:
        print(f'Unable to parse {line}')
print(parsed_config)

#test 6
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Total water left after {days_left} days is: {total_water_left} liters"

print( water_left(5, 100, 2) )

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        #print(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

try:
    print( water_left(5, 100, 2) )
except RuntimeError as err:
    #alert_navigation_system(err)
    print(err)

#test 7
def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

try:
    print( water_left(5, 100, None) )
except RuntimeError as err1:
    #alert_navigation_system(err)
    print(err1)
except TypeError as err2:
    #alert_navigation_system(err)
    print(err2)

#exam 1
true_values = ['yes', 'y']
false_values = ['no', 'n']

def str_to_bool(value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError('Invalid entry')

str_to_bool("y")
