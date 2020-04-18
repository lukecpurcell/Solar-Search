'''
'Solar Search'
Author: Lucas Purcell
(COP 1500 Integration Project)

    This program will provide information about the planets in our solar system.
'''

# IMPORTS:
# needed for the sleep function using in the function that asks the user if they want to rerun the program
from time import sleep

# Planet Data:

#SUN:
sun_dist = "≈ 149,668,992km"
sun_temp = "≈ 5505ºC"
sun_diam = "1,391,000km"
sun_mass = "1,300,000"
sun_fact = "The Sun accounts for 99.86% of the mass in the solar system!"

#Mercury:
mercury_dist = "0.39"
mercury_temp = "-180ºC to 430ºC"
mercury_orbit = "0.24 Earth Years"
mercury_grav = "0.38"
mercury_diam = "4,878km"
mercury_mass = "0.055"
mercury_fact = "Although Mercury is the closest planet to the sun,\n" \
               "ice can be found in permanent crater shadows!"

#VENUS:
venus_dist = "0.72"
venus_temp = "465ºC"
venus_orbit = "0.62 Earth Years"
venus_grav = "0.9"
venus_diam = "12,104km"
venus_mass = "0.815"
venus_fact = "Venus is the second brightest natural object in the sky after the moon!"

#EARTH:
earth_dist = "1"
earth_temp = "-89ºC to 58ºC"
earth_orbit = "1 Earth Year"
earth_grav = "1"
earth_diam = "12,756km"
earth_mass = "1"
earth_fact = "Earth is the only planet not named after a god."

#MARS:
mars_dist = "1.52"
mars_temp = "-89ºC to 0ºC"
mars_orbit = "1.88 Earth Years"
mars_grav = "0.38"
mars_diam = "6,787km"
mars_mass = "0.107"
mars_fact = "'Mars' is the name of the Roman god of war, who, according to Roman myth, rode\n" \
            "on a chariot pulled by two horses named 'Phobos' and 'Deimos'. Mars has two moons\n" \
            "which have been named after these horses."

#JUPITER:
jupiter_dist = "5.20"
jupiter_temp = "-150ºC"
jupiter_orbit = "11.86 Earth Years"
jupiter_grav = "2.64"
jupiter_diam = "142,800km"
jupiter_mass = "318"
jupiter_fact = "Jupiter is the fastest spinning planet in our solar system!"

#SATURN:
saturn_dist = "9.54"
saturn_temp = "-170ºC"
saturn_orbit = "29.46 Earth Years"
saturn_grav = "0.93"
saturn_diam = "120,000km"
saturn_mass = "95"
saturn_fact = "Saturn has a whopping 62 moons!"

#URANUS:
uranus_dist = "19.18"
uranus_temp = "-200ºC"
uranus_orbit = "84.01 Earth Years"
uranus_grav = "0.89"
uranus_diam = "51,118km"
uranus_mass = "15"
uranus_fact = "Uranus turns on its axis once every 17 hours, 14 minutes!"

#NEPTUNE:
neptune_dist = "30.06"
neptune_temp = "-210ºC"
neptune_orbit = "164.8 Earth Years"
neptune_grav = "1.12"
neptune_diam = "49,528km"
neptune_mass = "17"
neptune_fact = "Neptune has 6 faint rings and 14 known moons.\n" \
               "New moons are being discovered every couple of years."

#PLUTO:
pluto_dist = "39.44"
pluto_temp = "-220ºC"
pluto_orbit = "247.7 Earth Years"
pluto_grav = "0.06"
pluto_diam = "2,300km"
pluto_mass = "0.002"
pluto_fact = "Pluto is one 1/3 ice!"


# GREETING:
print("Hello! Welcome to Solar Search! In this program, you will type the name of a planet,\n"
      "and information about that planet will be shown!")


# gets user's name and age, while making sure the age is a positive number
# if not, it will ask for input again.
def greeting():
    while True:
        try:
            user_age = int(input("Please enter your age: "))
        except ValueError:
            print("Sorry, your age must be a number\n"
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
        user_name = input("Please enter your name: ")
        if (user_name.isdigit()):
            print("Sorry, your name can't be a number.\n"
                  "Please try again.")
            continue
        else:
            user_name = str(user_name)
            break

    greeting_statement = "Hello, " + user_name.capitalize() + "! " + user_age + " is the perfect age to learn about " \
                                                                       "the planets in our solar system!"
    print(greeting_statement)

greeting() #call to greeting function

print("-----------------------------------------")  # added for UI enhancements
sleep(1.5)

print("First, choose from the list below to learn about that planet (or the sun!) \n")

#list of planets to show the user their options
planets = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto\n']

#formats planet names into a numbered list
for index, value in enumerate(planets, 1):
    print("{}. {}".format(index, value))

# This function asks the user if they would like to enter another planet:
def rerun():
    while True:
        run_choice = input('Would you like to learn about a different planet? (yes/no): ')
        if run_choice == 'Yes' or run_choice == 'yes':
            break
        if run_choice == 'No' or run_choice == 'no':
            print("Thanks for using Solar Search!")
            print("Goodbye!")
            sleep(2.5)
            print("<<< PROGRAM TERMINATED >>>")
            quit()
        else:
            print("Invalid Input")
            print("Please try again!")

def main():
    while True:
        planet_selection = input("Please enter the name of a planet: ")
        planet_selection = planet_selection.upper()
        if planet_selection == 'SUN':  # SUN
            print("-----------------------------------------")
            print("You selected the sun.\n")
            print("Distance from Earth: %s\n" % sun_dist)
            print("Temperature: %s\n" % sun_temp)
            print("Diameter: %s\n" % sun_diam)
            print("Mass(Earth = 1): %s\n" % sun_mass)
            print("Fun Fact: %s\n" % sun_fact)
            rerun()
        elif planet_selection == 'MERCURY':  # MERCURY
            print("-----------------------------------------")
            print("You selected the planet Mercury.\n")
            print("Distance from the sun(AU): %s\n" % sun_dist)
            print("Temperature range: %s\n" % mercury_temp)
            print("Orbital period: %s\n" % mercury_orbit)
            print("Equatorial surface gravity(Earth = 1): %s\n" % mercury_grav)
            print("Mean diameter: %s\n" % mercury_diam)
            print("Mass(Earth = 1): %s\n" % mercury_mass)
            print("Fun Fact: %s\n" % mercury_fact)
            rerun()
        elif planet_selection == 'VENUS':  # VENUS
            print("-----------------------------------------")
            print("You selected the planet Venus.\n")
            print("Distance from the sun(AU): %s\n" % sun_dist)
            print("Temperature: %s\n" % venus_temp)
            print("Orbital period: %s\n" % venus_orbit)
            print("Equatorial surface gravity(Earth = 1): %s\n" % venus_grav)
            print("Mean diameter: %s\n" % venus_diam)
            print("Mass(Earth = 1): %s\n" % venus_mass)
            print("Fun Fact: %s\n" % venus_fact)
            rerun()
        elif planet_selection == 'EARTH':  # EARTH
            print("-----------------------------------------")
            print("You selected the planet Earth.\n")
            print("Distance from the sun(AU): %s\n" % sun_dist)
            print("Temperature range: %s\n" % earth_temp)
            print("Orbital period: %s\n" % earth_orbit)
            print("Equatorial surface gravity(Earth = 1): %s\n" % earth_grav)
            print("Mean diameter: %s\n" % earth_diam)
            print("Mass(Earth = 1): %s\n" % earth_mass)
            print("Fun Fact: %s\n" % earth_fact)
            rerun()
        elif planet_selection == 'MARS':  # MARS
            print("-----------------------------------------")
            print("You selected the planet Mars.\n")
            print("Distance from the sun(AU): %s\n" % sun_dist)
            print("Temperature range: %s\n" % mars_temp)
            print("Orbital period: %s\n" % mars_orbit)
            print("Equatorial surface gravity(Earth = 1): %s\n" % mars_grav)
            print("Mean diameter: %s\n" % mars_diam)
            print("Mass(Earth = 1): %s\n" % mars_mass)
            print("Fun Fact: %s\n" % mars_fact)
            rerun()
        elif planet_selection == 'JUPITER':  # JUPITER
            print("-----------------------------------------")
            print("You selected the planet Jupiter.\n")
            print("Distance from the sun(AU): %s\n" % sun_dist)
            print("Temperature: %s\n" % jupiter_temp)
            print("Orbital period: %s\n" % jupiter_orbit)
            print("Equatorial surface gravity(Earth = 1): %s\n" % jupiter_grav)
            print("Mean diameter: %s\n" % jupiter_diam)
            print("Mass(Earth = 1): %s\n" % jupiter_mass)
            print("Fun Fact: %s\n" % jupiter_fact)
            rerun()
        elif planet_selection == 'SATURN':  # SATURN
            print("-----------------------------------------")
            print("You selected the planet Saturn.\n")
            print("Distance from the sun(AU): %s\n" % sun_dist)
            print("Temperature: %s\n" % saturn_temp)
            print("Orbital period: %s\n" % saturn_orbit)
            print("Equatorial surface gravity(Earth = 1): %s\n" % saturn_grav)
            print("Mean diameter: %s\n" % saturn_diam)
            print("Mass(Earth = 1): %s\n" % saturn_mass)
            print("Fun Fact: %s\n" % saturn_fact)
            rerun()
        elif planet_selection == 'URANUS':  # URANUS
            print("-----------------------------------------")
            print("You selected the planet Uranus.\n")
            print("Distance from the sun(AU): %s\n" % sun_dist)
            print("Temperature: %s\n" % uranus_temp)
            print("Orbital period: %s\n" % uranus_orbit)
            print("Equatorial surface gravity(Earth = 1): %s\n" % uranus_grav)
            print("Mean diameter: %s\n" % uranus_diam)
            print("Mass(Earth = 1): %s\n" % uranus_mass)
            print("Fun Fact: %s\n" % uranus_fact)
            rerun()
        elif planet_selection == 'NEPTUNE':  # NEPTUNE
            print("-----------------------------------------")
            print("You selected the planet Neptune.\n")
            print("Distance from the sun(AU): %s\n" % sun_dist)
            print("Temperature: %s\n" % neptune_temp)
            print("Orbital period: %s\n" % neptune_orbit)
            print("Equatorial surface gravity(Earth = 1): %s\n" % neptune_grav)
            print("Mean diameter: %s\n" % neptune_diam)
            print("Mass(Earth = 1): %s\n" % neptune_mass)
            print("Fun Fact: %s\n" % neptune_fact)
            rerun()
        elif planet_selection == 'PLUTO':  # PLUTO
            print("-----------------------------------------")
            print("You selected the 'planet' Pluto.\n")
            print("Distance from the sun(AU): %s\n" % sun_dist)
            print("Temperature: %s\n" % pluto_temp)
            print("Orbital period: %s\n" % pluto_orbit)
            print("Equatorial surface gravity(Earth = 1): %s\n" % pluto_grav)
            print("Mean diameter: %s\n" % pluto_diam)
            print("Mass(Earth = 1): %s\n" % pluto_mass)
            print("Fun Fact: %s\n" % pluto_fact)
            rerun()
        else:
            print("Please check your spelling and try again!")

main()

'''
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
    
'''
