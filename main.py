"""
'Solar Search' VERSION 2.0
Author: Lucas Purcell
(COP 1500 Integration Project)
    This program will provide information about the planets in our solar system.
"""

print("Hello! Welcome to Solar Search! In this program, you will type the name of a planet,\n"
      "and information about that planet will be shown!")

while True:
    try:
        user_age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, your age must be a whole number\n"
              "Please try again.")
        continue
    if user_age < 1:
        print("Sorry, your age must be positive.\n"
              "Please try again.")
        continue
    else:
        user_age = str(user_age)
        break

while True:
    try:
        user_name = input("Please enter your name: ")
    except ValueError:
        print("Sorry, your name can't be a number.\n"
              "Please try again.")
        continue
    else:
        user_name = str(user_name)
        break

print("Hello, " + user_name.capitalize() + "! " + user_age + " is the perfect age to learn about "
                                                             "the planets in our solar system!")


def display_planet_data(name, dist, temp, orbit, grav, diam, mass):
    """Creates a display of information that correlates
    to the selected planet (name)."""
    print("Name: " + name)
    print("Distance from the sun: " + dist)
    print("Temperature range: " + temp)
    print("Orbital period: " + orbit)
    print("Equatorial surface gravity(Earth = 1): " + grav)
    print("Mean diameter: " + diam)
    print("Mass(Earth = 1): " + mass)


print("Please choose from the list below to learn about that planet. \n")


# list of planets to show the user their options
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto\n']

# formats planet names into a numbered list
for index, value in enumerate(planets, 1):
    print("{}. {}".format(index, value))


def mercury():
    display_planet_data(name='Mercury', dist='0.39', temp='-180ºC to 430ºC', orbit='0.24 Earth Years', grav='0.38',
                        diam='4,878km', mass='0.055')


def venus():
    display_planet_data(name='Venus', dist='0.72', temp='465ºC', orbit='0.62 Earth Years', grav='0.9', diam='12,104km',
                        mass='0.815')


def earth():
    display_planet_data(name='Earth', dist='1', temp='-89ºC to 58ºC', orbit='1 Earth Year', grav='1', diam='12,756km',
                        mass='1')


def mars():
    display_planet_data(name='Mars', dist='0.72', temp='465ºC', orbit='0.62 Earth Years', grav='0.9', diam='12,104km',
                        mass='0.815')


def jupiter():
    display_planet_data(name='Jupiter', dist='5.20', temp='-150ºC', orbit='11.86 Earth Years', grav='2.64',
                        diam='142,800km', mass='318')


def saturn():
    display_planet_data(name='Saturn', dist='9.54', temp='-170ºC', orbit='29.46 Earth Years', grav='0.93',
                        diam='120,000km', mass='95')


def uranus():
    display_planet_data(name='Uranus', dist='19.18', temp='-200ºC', orbit='84.01 Earth Years', grav='0.89',
                        diam='51,118km', mass='15')


def neptune():
    display_planet_data(name='Neptune', dist='30.06', temp='-210ºC', orbit='164.8 Earth Years', grav='1.12',
                        diam='49,528km', mass='17')


def pluto():
    display_planet_data(name='Pluto', dist='39.44', temp='-220ºC', orbit='247.7 Earth Years', grav='0.06',
                        diam='2,300km', mass='0.002')


def rerun():
    while True:
        run_choice = input(
            'Would you like to learn about a different planet?: ')  # maybe include an is.upper command after this line
        run_choice = run_choice.upper()
        if run_choice == 'YES':
            break
        elif run_choice == 'NO':
            print("Thanks for using Solar Search!")
            print("Goodbye!")
            print("<<< PROGRAM TERMINATED >>>")
            quit()
        else:
            print("Invalid Input")
            print("Please try again!")


def main():
    """Calls the appropriate function for each planet that is requested
    by the user. If the user would like to view another planet, they are asked which planet."""
    while True:
        user_input = input(str('Type planet here: '))
        user_input = user_input.lower()
        if user_input == 'mercury':
            mercury()
            rerun()
        elif user_input == 'venus':
            venus()
            rerun()
        elif user_input == 'earth':
            earth()
            rerun()
        elif user_input == 'mars':
            mars()
            rerun()
        elif user_input == 'jupiter':
            jupiter()
            rerun()
        elif user_input == 'saturn':
            saturn()
            rerun()
        elif user_input == 'uranus':
            uranus()
            rerun()
        elif user_input == 'neptune':
            neptune()
            rerun()
        elif user_input == 'pluto':
            pluto()
            rerun()
        else:
            print('please check your spelling and try again')


main()

"""
CITATIONS:
Planet Data:
    https://www.windows2universe.org/our_solar_system/planets_table.html
    https://www.universetoday.com/33415/interesting-facts-about-the-planets/
    https://mars.nasa.gov/all-about-mars/facts/
    https://www.universetoday.com/15182/interesting-facts-about-jupiter/
    https://theplanets.org/the-sun/
Python Help:
    https://docs.python.org/3/library/time.html
    https://www.w3schools.com/python/python_try_except.asp
    https://www.programiz.com/python-programming/break-continue
"""
