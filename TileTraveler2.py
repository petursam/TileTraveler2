# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
LIST_OF_LEVER_ROOMS = [(1,2),(2,2),(2,3),(3,2)]

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")

def pull_a_lever(amount_of_coins):
    
    lever_pull = input("Pull a lever (y/n): ")
    lever_pull = lever_pull.lower()
    if lever_pull == "y":
        amount_of_coins = amount_of_coins + 1 
        print("You received 1 coin, your total is now {}.".format(amount_of_coins))
    return amount_of_coins


def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions, amount_of_coins):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        if (col, row) in LIST_OF_LEVER_ROOMS:
            amount_of_coins = pull_a_lever(amount_of_coins)
    return victory, col, row, amount_of_coins

def again():
    play_again = input("Play again (y/n): ")
    play_again.lower()
    if play_again == "y":
        play()
    else:
        None
# The main program starts here
def play():
    victory = False
    row = 1
    col = 1
    amount_of_coins = 0

    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, amount_of_coins = play_one_move(col, row, valid_directions,amount_of_coins)
        
    print("Victory! Total coins {}.".format(amount_of_coins))
    again()
play()