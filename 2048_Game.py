# Importing the necessary libraries
import random

# Initializing the list
l = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#Printing the board
def PrintBoard(q) :
    print(f"{q[0][0]}  {q[0][1]}  {q[0][2]}  {q[0][3]} \n{q[1][0]}  {q[1][1]}  {q[1][2]}  {q[1][3]} \n{q[2][0]}  {q[2][1]}  {q[2][2]}  {q[2][3]} \n{q[3][0]}  {q[3][1]}  {q[3][2]}  {q[3][3]}")
    print(f"----------------------------------------")
# Left side movements
def move_left(q):
    for i in range(0, 4):
        for j in range(1, 4):  # Fixing the range for j
            recur_left(i, j, q)

def recur_left(i, j, q):
    if j <= 0:
        return  # Reached the leftmost column of the grid
    elif q[i][j-1] == 0:
        q[i][j-1] = q[i][j]
        q[i][j] = 0
        recur_left(i, j-1, q)  # Move one step left and continue recursively
    elif q[i][j-1] == q[i][j]:
        q[i][j-1] *= 2
        q[i][j] = 0
    # If the cell to the left is not empty or has a different value, stop recursion

# Right side movements
def move_right(q):
    for i in range(0, 4):
        for j in range(2, -1, -1):  # Fixing the range for j
            recur_right(i, j, q)

def recur_right(i, j, q):
    if j >= 3:
        return  # Reached the rightmost column of the grid
    elif q[i][j+1] == 0:
        q[i][j+1] = q[i][j]
        q[i][j] = 0
        recur_right(i, j+1, q)  # Move one step right and continue recursively
    elif q[i][j+1] == q[i][j]:
        q[i][j+1] *= 2
        q[i][j] = 0
    # If the cell to the right is not empty or has a different value, stop recursion

# Up movement
def move_up(q):
    for i in range(1, 4):  # Fixing the range for i
        for j in range(0, 4):
            recur_up(i, j, q)

def recur_up(i, j, q):
    if i <= 0:
        return  # Reached the top of the grid
    elif q[i-1][j] == 0:
        q[i-1][j] = q[i][j]
        q[i][j] = 0
        recur_up(i-1, j, q)  # Move one step up and continue recursively
    elif q[i-1][j] == q[i][j]:
        q[i-1][j] *= 2
        q[i][j] = 0
    # If the cell above is not empty or has a different value, stop recursion

# Down movement
def move_down(q):
    for i in range(2, -1, -1):  # Fixing the range for i
        for j in range(0, 4):
            recur_down(i, j, q)

def recur_down(i, j, q):
    if i >= 3:
        return  # Reached the bottom of the grid
    elif q[i+1][j] == 0:
        q[i+1][j] = q[i][j]
        q[i][j] = 0
        recur_down(i+1, j, q)  # Move one step down and continue recursively
    elif q[i+1][j] == q[i][j]:
        q[i+1][j] *= 2
        q[i][j] = 0
    # If the cell below is not empty or has a different value, stop recursion

# Adding 2 randomly
def add_random(q):
    if check_for_zero(q):
        random.seed()
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        pp = [2, 4]
        c = random.choice(pp)
        if q[x][y] == 0:
            q[x][y] = c
        else:
            add_random(q)

# Checks for zero
def check_for_zero(lst):
    for sub_lst in lst:
        if 0 in sub_lst:
            return True
    return False

# Checks for 2048
def check_for_2048(lst):
    for sub_lst in lst:
        if 2048 in sub_lst:
            return True
    return False

# Checks to see if the game is to be continued
def Game_Won_Lost(lst):
    if not (check_for_zero(lst)):
        print('Game Over')
        return False
    elif (check_for_2048(lst)):
        print('You have won')
        return False
    else:
        return True

# Basic move
def move(a):
    print("Commands are as follows: \n'W' or 'w': Move Up\n'S' or 's': Move Down\n'L' or 'l': Move Left\n'R' or 'r': Move Right")
    q = input("Enter your move: ")
    q = q.lower()
    if q == 'w':
        PrintBoard(l)
        move_up(l)
        PrintBoard(l)
    elif q == 's':
        PrintBoard(l)
        move_down(l)
        PrintBoard(l)
    elif q == 'l':
        PrintBoard(l)
        move_left(l)
        PrintBoard(l)
    elif q == 'r':
        PrintBoard(l)
        move_right(l)
        PrintBoard(l)

while Game_Won_Lost(l):
    add_random(l)
    move(l)
