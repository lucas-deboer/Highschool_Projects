# Lucas DeBoer
# Tic Tac Toe
# April 20

# testing to see if this change also is reflected in Github.com

# import statements & variable setup
from random import choice

sample = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
wins = 0
Game = True


# Functions --------------------------------------------------------------------------------------
# Printing the game "display"
def printTable(squares):
    print()
    counter = 0  # used to get the value (x,y,or space) placed on each square
    for x in range(3):
        print("", squares[counter], "", end="")  # get the value (x,y,or space) placed on that square
        counter += 1
        print("|", end="")
        print("", squares[counter], "", end="")
        counter += 1
        print("|", end="")
        print("", squares[counter], "")
        counter += 1
        if x != 2:
            print("-----------")


# choose a random number
def randomizer(x):
    rand = choice(x)  # squares are placed completely randomly
    while squares[rand] != " ":
        rand = choice(x)
    squares[rand] = token
    print("\nThe computer placed a token on space", rand + 1)


# check win: check if there are three tiles in a row
def checkWin(squares):
    for x in range(3):
        if squares[x * 3] == squares[x * 3 + 1] == squares[x * 3 + 2] and squares[x * 3] != " ":
            return squares[x * 3]  # check the rows
        if squares[x] == squares[x + 3] == squares[x + 6] and squares[x] != " ":
            return squares[x]  # check the columns
    if ((squares[0] == squares[4] == squares[8]) or (squares[2] == squares[4] == squares[6])) and squares[4] != " ":
        return squares[4]


# Used when a player is placing a token
def placeToken(playerName, token, squares):
    while True:
        slot = input("\nPlayer {}, please select a space to place your token: ".format(playerName))
        if slot in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            if squares[int(slot) - 1] == " ":
                squares[int(slot) - 1] = token
                return squares
            print("There is already a token on this space, choose another space.")
        else:
            print("Please choose a space between 1-9.")


# check the next turn (can be used to win or block)
def checkNext(squares, token, switch):
    if switch:
        token = "X" if token == "O" else "O"
    for x in range(9):
        if squares[x] == " ":
            squares[x] = token
            if checkWin(squares) is None:
                squares[x] = " "
                return x
            else:
                squares[x] = " "


# Computer token placer (based upon difficulty)
def computerToken(token, squares, difficulty, turnNum):
    if difficulty == "1":  # easy difficulty
        randomizer(range(0, 9))
    elif difficulty == "2":  # medium difficulty
        winNext = checkNext(squares, token, False)  # calculate once to save time
        blockNext = checkNext(squares, token, True)
        if winNext is not None:  # first check if the computer can win
            squares[winNext] = token
            print("The computer placed a token on space", winNext + 1)
        elif blockNext is not None:  # then block the opponent
            squares[blockNext] = token
            print("The computer placed a token on space", blockNext + 1)
        elif " " in squares[::2]:
            randomizer((0, 2, 4, 6, 8))
        else:
            randomizer((1, 3, 5, 7))
    else:  # impossible difficulty
        winNext = checkNext(squares, token, False)  # calculate once to save time
        blockNext = checkNext(squares, token, True)
        if winNext is not None:  # first check if the computer can win
            squares[winNext] = token
            print("The computer placed a token on space", winNext + 1)
        elif blockNext is not None:  # then block the opponent
            squares[blockNext] = token
            print("The computer placed a token on space", blockNext + 1)
        elif token == "X":  # if the computer starts, it will play to win, as in most cases, it can
            if squares[0] == " ":  # always start with space 1 (for simplicity)
                squares[0] = "X"
            elif squares[8] == "O" and squares[4] != "X":  # Case: They play opposite of you
                if squares[6] == " ":
                    squares[6] = "X"  # They will block in between
                else:
                    squares[2] = "X"  # place far corner to win automatically
            elif "O" in (squares[2], squares[6]):  # Case: they play on a corner beside
                if squares[8] == " ":
                    squares[8] = "X"  # They should block in between
                    print("The computer placed a token on space 9.")
            elif "O" in (squares[1], squares[3]):  # Case: they play middle close
                if squares[4] == " ":
                    squares[4] = "X"  # place in center regardless ;)
                    print("The computer placed a token on space 5.")
                elif squares[1] == "O":  # play corner opposite of side they chose
                    squares[6] = "X"
                    print("The computer placed a token on space 7.")
                else:
                    squares[2] = "X"
                    print("The computer placed a token on space 3.")
            elif "O" in (squares[5], squares[7]):  # Case: they play middle far
                if squares[2] == " ":  # place top right corner
                    squares[2] = "X"
                    print("The computer placed a token on space 3.")
                else:
                    squares[4] = "X"  # win with the middle
                    print("The computer placed a token on space 5.")
            else:  # center space - win or tie
                if squares[8] == " ":  # always play opposite
                    squares[8] = "X"
                    print("The computer placed a token on space 9.")
        else:  # when computer doesn't start (token = "O"), play to tie
            if squares[4] == " ":  # always take the center first
                squares[4] = "O"
                print("The computer placed a token on space 5.")
            elif "X" in (squares[0], squares[2], squares[6], squares[8]) and squares[4] != "X" and turnNum <= 4:
                # Case: corner
                if (squares[0] == "X" and squares[8] == "X") or (
                        squares[2] == "X" and squares[6] == "X"):  # Then they go opposite
                    randomizer((1, 3, 5, 7))
                else:  # either of the far middle blocks
                    # and "X" not in (squares[1],squares[2],squares[3],squares[4],squares[6],squares[8]):
                    if (squares[5] == "X" != squares[7] or squares[7] == "X" != squares[5]) and squares[0] == "X":
                        squares[8] = "O"
                        print("The computer placed a token on space 9.")
                    elif (squares[1] == "X" != squares[3] or squares[3] == "X" != squares[1]) and squares[8] == "X":
                        # and "X" not in (squares[0],squares[2],squares[4],squares[5], squares[6],squares[7]):
                        squares[0] = "O"
                        print("The computer placed a token on space 1.")
                    elif (squares[3] == "X" != squares[7] or squares[7] == "X" != squares[3]) and squares[2] == "X":
                        # and "X" not in (squares[0], squares[1],squares[4],squares[5], squares[6],squares[8]):
                        squares[6] = "O"
                        print("The computer placed a token on space 7.")
                    elif (squares[5] == "X" != squares[1] or squares[1] == "X" != squares[5]) and squares[6] == "X":
                        # and "X" not in (squares[0],squares[2],squares[3],squares[4],squares[7],squares[8]):
                        squares[2] = "O"
                        print("The computer placed a token on space 3.")

            # Case: middle then adjacent middle
            elif "X" in (squares[1], squares[3], squares[5], squares[7]) and turnNum <= 4:
                if "X" == squares[1] == squares[3]:
                    squares[0] = "O"
                    print("The computer placed a token on space 1.")
                elif "X" == squares[1] == squares[5]:
                    squares[2] = "O"
                    print("The computer placed a token on space 3.")
                elif "X" == squares[3] == squares[7]:
                    squares[6] = "O"
                    print("The computer placed a token on space 7.")
                elif "X" == squares[5] == squares[7]:
                    squares[8] = "O"
                    print("The computer placed a token on space 9.")
            else:
                if " " in (squares[0], squares[2], squares[6], squares[8]):
                    randomizer((0, 2, 6, 8))
                else:
                    randomizer((1, 3, 5, 7))
    return squares


# Header / Menu --------------------------------------------------------------------------------------
print("Tic-Tac-Toe!\n------------------------------")

while True:  # Run through the menu until the desired settings are achieved
    while True:  # Choose One or Two Player
        mode = input("Type '1' to play against the computer or '2' to play 2-player mode: ")
        if mode == "1" or mode == "2":
            break
        print("Please choose either '1' or '2'.")

    if mode == "1":  # determine the difficulty if single player mode is chosen
        print("There are 3 difficulty levels: ")
        print("1 - Easy. The computer places tokens randomly.")
        print("2 - Hard. The computer will try to block you and places tokens somewhat intelligently.")
        print("3 - Impossible. The computer can not be beat.")
        while True:
            difficulty = input("Please choose a difficulty level from 1-3: ")
            if difficulty in ("1", "2", "3"):
                break
            print("Please choose either '1', '2', or '3'.")
        print("You have chosen to play against the computer (single player mode), with difficulty level", difficulty)
    else:
        difficulty = "0"
        print("You have chosen to play 2-player mode.")

    while True:  # check to see if the player is satisfied with their choices, if not, restart the process.
        proceed = input("Are these your desired settings ('y' or 'n'): ")
        if proceed == "y" or proceed == "n":
            break
    if proceed == "y":
        break

# Final Rules --------------------------------------------------------------------------------------
print("\nThe first player to get three tokens in a row horizontally, vertically, or diagonally wins!")
print("On your turn, when prompted to place your token enter a number from 1-9.")
print("The top left corner is '1', and the bottom right corner is '9'.")
print("This table shows the number of each space.")
printTable(sample)
print("\nGood Luck!")

# Gameplay --------------------------------------------------------------------------------------
while Game:
    squares = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    if choice((0, 1)) == 0:  # randomly choose who starts
        print("\nPlayer 1 starts.")
        player1Turn = True
    else:
        player1Turn = False
        if mode == "2":
            print("\nPlayer 2 starts.")
        else:
            print("\nThe computer starts.")
    # The Actual Game ---------------------------------------------------------------------------------------------
    for x in range(1, 10):  # maximum of nine turns
        playerName = "1" if player1Turn is True else "2"  # who's turn it is
        token = "X" if x % 2 != 0 else "O"  # what token is being placed
        if difficulty == "0" or player1Turn is True:
            squares = placeToken(playerName, token, squares)
        else:
            squares = computerToken(token, squares, difficulty, x)
        printTable(squares)
        if checkWin(squares) is not None:  # break out earlier if there is a winner
            break
        player1Turn = not player1Turn

    # determine the winner --------------------------------------------------------------------------------------
    if checkWin(squares) is None:
        print("\nCat's game, no winner.")
    elif player1Turn:
        wins += 1
        print("\nCongratulations Player 1, you won!")
    else:
        if difficulty == "0":
            print("\nCongratulations Player 2, you won!")
        else:
            print("\nBetter luck next time, the computer won.")
    # Ask if they want to play again
    while True:  # check to see if the player is satisfied with their choices, if not, restart the process.
        encore = input("Do you want to play again with the same settings ('y' or 'n'): ")
        if encore == "y" or encore == "n":
            break
    if encore == "n":
        break
if wins == 0 or wins > 1:
    print("Congratulations, you won", wins, "games!")
else:
    print("You only won one game.")
