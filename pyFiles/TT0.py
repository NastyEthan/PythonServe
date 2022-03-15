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

