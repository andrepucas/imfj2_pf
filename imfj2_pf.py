# Projeto Final (A) de IMFJ2
# 2º Semestre 2019/2020
# André Santos 21901767

# Main messages
TXT_MENU = """
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||
|| What problem do you want to solve?
|| 1. Floatation
|| 2. Springs
||
|| (help): Type <help> for additional information.
||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""

TXT_FLOAT = """
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||
|| FLOATATION - CURRENT PARAMETERS:
||
|| CUBE:
|| <cube> density  = {0} kg/m^3 
|| <mass>          = {1} kg 
|| <volume>        = {2} m^3
||
|| ENVIRONMENT:
|| <fluid> density = {3} kg/m^3 
|| <gravity>       = {4} m/s
||
|| From it's center, the cube sinks: {5} m.
|| 
|| (help): Type <help> for additional information.
||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""

TXT_SPRING = """
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||
|| CEILING SPRING - CURRENT PARAMETERS:
||
|| SPRING:
|| <rest> length   = {0} m
|| <constant>      = {1} N/m 
||
|| ENVIRONMENT:
|| <mass>          = {2} kg
|| <gravity>       = {3} m/s
||
|| The spring would stretch to: {4} m.
|| 
|| (help): Type <help> for additional information.
||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""

# Help messages
TXT_HELP_M = """
???????????????????????????????????????????????????????????????????
??
?? (help): -> Type in <1> or <2> and press Enter to choose.
??         -> <quit> at any time closes the program.
??         -> <menu> shows you the menu again.
??
???????????????????????????????????????????????????????????????????"""

TXT_HELP_F = """
???????????????????????????????????????????????????????????????????
??
?? (help): -> Examples: 
??         -> <set fluid 500> sets fluid value to 500.
??         -> <quit> closes the program.
??         -> <menu> returns you to the main menu.
??
???????????????????????????????????????????????????????????????????"""

TXT_HELP_S = """
???????????????????????????????????????????????????????????????????
??
?? (help): -> Examples: 
??         -> <set rest 1> sets rest value to 1.
??         -> <quit> closes the program.
??         -> <menu> returns you to the main menu.
??
???????????????????????????????????????????????????????????????????"""

# Error message
TXT_ERROR = """
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!
!! (error): -> Invalid inputs. Failed to understand what you want.
!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""

### Menu
def menu():
    print(TXT_MENU)

    # Waits for user to input one of the options
    user_i = ""
    while (user_i != "quit"):
        print("")
        user_i = input(">> ")
        user_i = user_i.strip().lower()

        # Starts floatation problem
        if (user_i[0] == "1" or user_i == "floatation"):
            floatation()

        # Starts springs problem
        elif (user_i[0] == "2" or user_i == "springs"):
            springs()

        # Help box
        elif (user_i == "help"):
            print(TXT_HELP_M)

        # Shows this menu again
        elif (user_i == "menu"):
            print(TXT_MENU)

        # Ignores mistakes
        else:
            continue

### Flotation problem
def floatation():
    cube = 500
    mass = 4000
    volume = 8
    fluid = 1000
    gravity = 9.81
    edge = volume ** (1/3)
    center = edge / 2

    # Appears before while loop to show an example to the user 
    updateF(cube, mass, volume, fluid, gravity, edge, center)

    while True:
        print("")
        user_i = input(">> ")
        user_i = user_i.strip().lower().split()

        if (user_i[0] == "set"):

            # Set cube density
            if (user_i[1] == "cube"):
                cube = float(user_i[2])
                # Mass needs to be updated
                mass = cube * volume
                updateF(cube, mass, volume, fluid, gravity, edge, center)

            # Set mass
            elif (user_i[1] == "mass"):
                mass = float(user_i[2])
                # Volume needs to be updated
                volume = mass / cube
                updateF(cube, mass, volume, fluid, gravity, edge, center)

            # Set volume
            elif (user_i[1] == "volume"):
                volume = float(user_i[2])
                # Mass needs to be updated
                mass = cube * volume
                updateF(cube, mass, volume, fluid, gravity, edge, center)

            # Set fluid density
            elif (user_i[1] == "fluid"):
                fluid = float(user_i[2])
                updateF(cube, mass, volume, fluid, gravity, edge, center)

            # Set gravity
            elif (user_i[1] == "gravity"):
                gravity = float(user_i[2])
                updateF(cube, mass, volume, fluid, gravity, edge, center)

            # Error box
            else:
                print(TXT_ERROR)
                print(TXT_HELP_F)

        # Help box
        elif (user_i[0] == "help"):
            print(TXT_HELP_F)

        # Returns to menu
        elif (user_i[0] == "menu"):
            menu()
            # exit() in case the user goes to the menu and types quit there
            exit()

        # Closes program
        elif (user_i[0] == "quit"):
            exit()

        # Error box
        else:
            print(TXT_ERROR)
            print(TXT_HELP_F)

### Updates Floatation Board - A separate function for this allows for the 
### board to only be updated when new values are inserted, instead of every
### cycle, which resulted in error/help messages staying hidden behind a
### repeated board.
def updateF(cube, mass, volume, fluid, gravity, edge, center):
    # RELATIVE DEPTH WITH CENTER OF THE CUBE - EXPLAINED
    # Gravitational Force = Buoyancy Force <=>
    # mass * gravity = fluid * gravity * volumeSubmerged <=>
    # mass = fluid * volumeSubmerged <=>
    volumeSubmerged = mass / fluid
    # volumeSubmerged = edge * edge * edgeSubmerged <=>
    edgeSubmerged = volumeSubmerged / (edge * edge)
    depth = edgeSubmerged - center

    print(TXT_FLOAT.format(cube, mass, volume, fluid, gravity, depth))


### Springs problem
def springs():
    rest = 0.2
    constant = 50
    mass = 2
    gravity = 9.81
    gF = mass * gravity

    # Appears before while loop to show an example to the user 
    updateS(rest, constant, mass, gravity, gF)

    while True:
        print("")
        user_i = input(">> ")
        user_i = user_i.strip().lower().split()

        if (user_i[0] == "set"):

            # Set spring rest length
            if (user_i[1] == "rest"):
                rest = float(user_i[2])
                updateS(rest, constant, mass, gravity, gF)

            # Set spring constant
            elif (user_i[1] == "constant"):
                constant = float(user_i[2])
                updateS(rest, constant, mass, gravity, gF)

            # Set object mass
            elif (user_i[1] == "mass"):
                mass = float(user_i[2])
                # gF needs to be updated
                gF = mass * gravity
                updateS(rest, constant, mass, gravity, gF)

            # Set gravity
            elif (user_i[1] == "gravity"):
                gravity = float(user_i[2])
                # gF needs to be updated
                gF = mass * gravity
                updateS(rest, constant, mass, gravity, gF)

            # Error box
            else:
                print(TXT_ERROR)
                print(TXT_HELP_S)

        # Help box
        elif (user_i[0] == "help"):
            print(TXT_HELP_S)

        # Returns to menu
        elif (user_i[0] == "menu"):
            menu()
            # exit() in case the user goes to the menu and types quit there
            exit()

        # Closes program
        elif (user_i[0] == "quit"):
            exit()

        # Error box
        else:
            print(TXT_ERROR)
            print(TXT_HELP_S)

### Updates Springs Board - Just like updateF(), this allows for error/help 
### messages to not get buried under a new repeated values board.
def updateS(rest, constant, mass, gravity, gF):
    # SPRING VERTICAL STRETCH - EXPLAINED
    # Gravitational Force + Spring Force = 0 <=>
    # - gravity * mass + (-constant * (stretch + rest)) = 0 <=>
    # - gF - (constant * stretch) - (constant * rest) = 0 <=>
    # - (constant * stretch) = gF + (constant * rest) <=>
    # - stretch = (gF + (constant*rest)) / - constant <=>
    stretch = (gF + (constant*rest)) / constant

    print(TXT_SPRING.format(rest, constant, mass, gravity, stretch))

# Program starts running here
menu()