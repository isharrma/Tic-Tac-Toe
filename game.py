from IPython.display import clear_output

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
flag = 8
player = 1
win = 0
is_draw = 0

# prints the board
def print_board():                                         
    print(board[0], " | " + board[1] + " | " + board[2])
    print("------------")
    print(board[3], " | " + board[4] + " | " + board[5])
    print("------------")
    print(board[6], " | " + board[7] + " | " + board[8])

# Initializes the Game
def startgame():                                            
    print_board()
    print("Choose a Position: ")
    
# Set X at given position by Player1
def p1(a):                                              
    global flag
    if a > 9:
        print("Invalid Move")
    elif board[a]=="X" or board[a] == "O":
        print("Position Already Occupied")
    else:
        board[a] = "X"
    flag = flag - 1

# Set O at given position by Player2
def p2(a):                                               
    global flag
    if a > 9:
        print("Invalid Move")
    elif board[a]=="X" or board[a] == "O":
        print("Position Already Occupied")
    else:
        board[a] = "O"
    flag = flag - 1

 # prints X or O
def move(a):                                              
    if player == 1:
        p1(a)
    else:
        p2(a)
    print_board()
    print()

# Controls which Player has the chance
def change():                                                 
    global player
    if player == 1:
        player = 2
    else:
        player = 1

# Check for Win Horizontally
def horizontal():                                              
    global win
    if (board[0] == board[1] == board[2]!="-") or (board[3] == board[4] == board[5]!="-") or (board[6] == board[7] == board[8]!="-"):
                win = 1

# Check for Win Vertically
def vertical():                                                
    global win
    if (board[0] == board[3] == board[6]!="-") or (board[1] == board[4] == board[7]!="-") or (board[2] == board[5] == board[8]!="-"):
                win = 1

 # Check for Win Diagonally
def diagonal():                                              
    global win
    if (board[0] == board[4] == board[8]!="-") or (board[2] == board[4] == board[6]!="-"):
                win = 1

 # Check for Win
def check():                                                
    global win
    horizontal()
    vertical()
    diagonal()
    if win==1:
        print("You Won! Player " + str(player))

  # Checks for Draw
def draw():                                               
    global is_draw
    if flag<0:
        print("Draw :(")
        is_draw = 1 


if __name__ == '__main__':
    startgame()
    try:
        while True:
            n = int(input())
            move(n-1)
            check()
            draw()
            if win == 1 or is_draw == 1:
                break
            change()
            clear_output(wait=True)
            
            
    except Exception as e:
        print(e)     
