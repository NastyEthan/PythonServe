import runpy
import TT0
import TT1
import TT2
import Swap
import Construct
import madlibs
import rockpaperscissors

# abstracted files in a folder (aka module)
# don't need since they're in the same file

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
]

# Submenu list of [Prompt, Action]
sub_menu0 = [
    ["Construct", Construct.mat],
    ["Pac", TT0.pac],
]

sub_menu = [
    ["Swap", Swap.swap],
    ["Loops/Lists", TT1.tester],
    ["Fibonacci", TT1.tester2],
    ["Factorials", TT2.ftester],
    ["Factors.Imperative", TT2.factors],
    ["Factors.OOP", TT2.testerfOOP],
    ["Palindrome", TT1.ethanpalindrome],
]

sub_menu1 = [
    ["Loops/Lists", TT1.tester],
]

sub_menu2 = [
    ["Mad Libs", madlibs.madlibs],
    ["Rock Paper Scissors", rockpaperscissors.rps],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Patterns", submenu0])
    menu_list.append(["Math Functions", submenu])
    menu_list.append(["Databases", submenu1])
    menu_list.append(["Games", submenu2])
    # menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def submenu1():
    title = "Function Submenu1" + banner
    buildMenu(title, sub_menu1)

def submenu0():
    title = "Function Submenu0" + banner
    buildMenu(title, sub_menu0)
  
def submenu2():
    title = "Function Submenu2" + banner
    buildMenu(title, sub_menu2)
  
def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
  menu()