from os import system  # To use clear screen


# List to make Board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-", ]


# Instructions Fuction
def instructions():
    _ = system('cls')
    print("     -------------")
    print("    ", "1", " | ", "2", " | ", "3")
    print("    ", "4", " | ", "5", " | ", "6")
    print("    ", "7", " | ", "8", " | ", "9")
    print("     -------------\n\n")
    print('''     Each Player Needs to enter number 
     according to above sample.

     Press any key to continue''')
    input()


# Function to display Board
def disp_board():
    _ = system('cls')
    print(f"\n    {name_1} (x)   vs  {name_2 } (o)\n")
    print("     -------------")
    print("    ", board[0], " | ", board[1], " | ", board[2])
    print("    ", board[3], " | ", board[4], " | ", board[5])
    print("    ", board[6], " | ", board[7], " | ", board[8])
    print("     -------------\n\n")


# Player 1 input
def player_1():
    # Player 1 = x
    player_1 = int(input(f"Enter a Number From 1-9 {name_1} : "))
    while board[player_1-1] != "-":
        print("Wrong Entry try again. ")
        player_1 = int(input("Player 1 Turn : "))  # Player 1 = x
    else:
        board[player_1-1] = "x"
        disp_board()


# Player 2 input
def palyer_2():
    # Player 2 = o
    player_2 = int(input(f"Enter a Number From 1-9 {name_2} : "))
    while board[player_2-1] != "-":
        print("Wrong Entry try again. ")
        player_2 = int(input("Player 2 Turn : "))  # Player 1 = x
    else:
        board[player_2-1] = "o"
        disp_board()


# To cheak win
def cheak_Win():
    won = False
    if board[0] == board[1] == board[2] == "x":
        print(f"Good Job {name_1} You Won. ")
        won = True
        return won
    elif board[3] == board[4] == board[5] == "x":
        print(f"Good Job {name_1} You Won. ")
        won = True
        return won
    elif board[6] == board[7] == board[8] == "x":
        print(f"Good Job {name_1} You Won. ")
        won = True
        return won
    elif board[0] == board[3] == board[6] == "x":
        print(f"Good Job {name_1} You Won. ")
        won = True
        return won
    elif board[1] == board[4] == board[7] == "x":
        print(f"Good Job {name_1} You Won. ")
        won = True
        return won
    elif board[2] == board[5] == board[8] == "x":
        print(f"Good Job {name_1} You Won. ")
        won = True
        return won
    elif board[0] == board[4] == board[8] == "x":
        print(f"Good Job {name_1} You Won. ")
        won = True
        return won
    elif board[2] == board[4] == board[6] == "x":
        print(f"Good Job {name_1} You Won. ")
        won = True
        return won
    elif board[0] == board[1] == board[2] == "o":
        print(f"Good Job {name_2} You Won. ")
        won = True
        return won
    elif board[3] == board[4] == board[5] == "o":
        print(f"Good Job {name_2} You Won. ")
        won = True
        return won
    elif board[6] == board[7] == board[8] == "o":
        print(f"Good Job {name_2} You Won. ")
        won = True
        return won
    elif board[0] == board[3] == board[6] == "o":
        print(f"Good Job {name_2} You Won. ")
        won = True
        return won
    elif board[1] == board[4] == board[7] == "o":
        print(f"Good Job {name_2} You Won. ")
        won = True
        return won
    elif board[2] == board[5] == board[8] == "o":
        print(f"Good Job {name_2} You Won. ")
        won = True
        return won
    elif board[0] == board[4] == board[8] == "o":
        print(f"Good Job {name_2} You Won. ")
        won = True
        return won
    elif board[2] == board[4] == board[6] == "o":
        print(f"Good Job {name_2} You Won. ")
        won = True
        return won

    return won


# To cheak a tie
def cheak_tie():
    if (board[0] != "-" and board[1] != "-" and board[2] != "-" and
        board[3] != "-" and board[4] != "-" and board[5] != "-" and
            board[6] != "-" and board[7] != "-" and board[8] != "-"):
        print("It is a tie.")
        exit()


# Function to take Turns from players
def game():
    while cheak_Win() == False:

        print(f"    {name_1}'s Turn \n\n")
        try:
            player_1()
        except:
            print("     !!!       WRONG INPUT        !!!")
            player_1()

        if cheak_Win() == True:
            exit()
        cheak_tie()

        print(f"    {name_2}'s Turn \n\n")
        try:
            palyer_2()
        except:
            print("     !!!       WRONG INPUT        !!!")
            palyer_2()

        if cheak_Win() == True:
            exit()
        cheak_tie()


# Main Function
if __name__ == "__main__":
    _ = system('cls')
    print(" *** *** ***   TIC TAC TOE *** *** ***\n")
    name_1 = input("\nEnter Player 1 Name : \n")
    name_2 = input("\nEnter Player 2 Name : \n")
    instructions()
    disp_board()
    game()
