# Data Structures Project
Here will be the code snippets for the individual project

{% includes replit.html %}

## Week 0
### PACMAN
```
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n")
    print(RESET_COLOR + "  " * 35)


# print pac with colors and leading spaces
def pac_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "    __         ___")
    print(sp + "   / o\\       /o o\\")
    print(sp + "  |   <  * *  |   |")
    print(sp + "   \\__/       |,,,|")
    print(RESET_COLOR)
          
# pac function, iterface into this file
def pac():
    # only need to print ocean once
    ocean_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate pac eating
    for position in range(start, distance, step):
        pac_print(position)  # call to function with parameter
        time.sleep(.1)
```

### DATABASE
```
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  # first entry
               "FirstName": "Michael",  
               "LastName": "Chicken",  
               "Team": "Bucks",  
               "Position": "Shooting Guard",  
               "FG": "100%",
               "Career Averages":["6.9 PPG", "9.5 APG", "4.2 RBG",".3 SPG","0.1 TOV"]  
              })  

InfoDb.append({  
               "FirstName": "Anirudh",  
               "LastName": "RamenChopin",  
               "Team": "Lakers",  
               "Position": "Point Guard",
               "FG": "69%",
               "Career Averages":["33.33 PPG","1.2 APG","8.2 RBG", "3.8 SPG", "0.5 TOV"]  
              })

InfoDb.append({  
               "FirstName": "Sahil",  
               "LastName": "Lamar Jackson Jr.",  
               "Team": "Rockets",  
               "Position": "Power Forward",  
               "FG": "40%",
               "Career Averages":["45.6 PPG","13.6 APG","9.2 RBG", "0.3 SPG", "3.2 TOV"]  
              })  

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"], InfoDb[n]["Team"], InfoDb[n]["Position"], InfoDb[n]["FG"])  # using comma puts space between values
    print("\t", "Career Averages:", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Career Averages"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
```

## Week 1


## Week 2


## Week 3


## Week 4

