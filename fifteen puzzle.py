import random
N=4
grid = [[0 for i in range(N)] for j in range(N)]

def print_grid():
    print('-' * ((N + 4) * N + N + 1))
    for i in range(N):
        print(end='|')
        for j in range(N):
            if grid[i][j] == 0:
                e = ' ' * (N + 4)
            else:
                str_len = len(str(grid[i][j]))
                r1 = ((N + 4) - str_len + 1) // 2
                r2 = ((N + 4) - str_len) - r1
                e = (' ' * r1) + str(grid[i][j]) + (' ' * r2)
            print(e, end='|')
        print()
        print('-' * ((N + 4) * N + N + 1))

#check win
def check_win():
    counter=1
    for i in range(N):
        for j in range(N):
            while (counter <= 15):
                if (grid[i][j]==counter):
                    counter=counter+1
                else:
                    return False
            return True


def read_grid():
    lis=[]
    for i in range(N):
        for j in range(N):
            if(grid[i][j]!=0):
                lis.append(grid[i][j])
    return lis

#function generate cells
def generate_cell():
    for i in range(N):
        for j in range (N):
           x=random.randint(0,15)+1
           while x in read_grid():
               x = random.randint(0, 15)+1
           grid[i][j] = x
    for i in range(N):
        for j in range(N):
            if grid[i][j]==16:
                grid[i][j]=0
                break
def check_available_direction_right(x,y):
    if(y==0):
        return False
    else:
        return True
def check_available_direction_left(x,y):
    if (y == 3):
        return False
    else:
        return True
def check_available_direction_down(x,y):
    if(x==0):
        return False
    else:
        return True
def check_available_direction_up(x,y):
    if(x==3):
        return False
    else:
        return True

def check_available_move(i,x,y):
    res = True

    if i == 3: res = check_available_direction_right(x,y)

    if i == 5: res = check_available_direction_up(x,y)

    if i == 1: res = check_available_direction_left(x,y)

    if i == 2: res = check_available_direction_down(x,y)
    return res


def move(i,x,y):
    if i==3:
        grid[x][y]=grid[x][y-1]
        grid[x][y-1]=0
    elif i==1:
        grid[x][y] = grid[x][y + 1]
        grid[x][y + 1] = 0
    elif i==5:
        grid[x][y] = grid[x+1][y]
        grid[x+1][y] = 0
    elif i==2:
        grid[x][y] = grid[x-1][y]
        grid[x-1][y] = 0


def check_valid_direction(i):
    if i == 1 or i == 2 or i == 3 or i == 5:
        return True
    else:
        return False

def check_emptyCell():
    for i in range(N):
        for j in range(N):
            if(grid[i][j]==0):
                return i,j

def grid_clear():
    for i in range(N):
        for j in range(N):
          grid[i][j]=0

def read_input(x,y):
    i = int(input('Enter the direction: '))
    while not check_valid_direction(i)  or not check_available_move(i,x,y) :
        i = int(input('Enter a valid direction: '))
    return i



# MAIN FUNCTION
def play_game():
    print("15puzzle Game!")
    print("Welcome...")
    print("============================")
    while True:
        print_grid()
        x,y=check_emptyCell()
        i = read_input(x,y)
        check_available_move(i, x, y)
        move(i,x,y)
        #if check win
        if check_win():
            # Prints the grid
            print_grid()
            # Announcement of the final statement
            print('Congrats, You won!')
            # Ask for continuing the game
            c = input('Continue [Y/N] ')
            if c not in 'yY':
                break

while True:
    grid_clear()
    generate_cell()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break