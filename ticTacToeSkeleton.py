### This part contains all the functions needed to run the game


### This function tells player what number to pick for each spot on the board.
def guideBoard():
    print "Refer to this board for the spot number:"
    print "   |   |"
    print " 0 | 1 | 2"
    print "   |   |"
    print "-----------"
    print "   |   |"
    print " 3 | 4 | 5"
    print "   |   |"
    print "-----------"
    print "   |   |"
    print " 6 | 7 | 8"
    print "   |   |"


### This function willl take in a list of 9 items and display each item. To display the item in the list, we do list[x], where [x] begins with 0, instead of 1.
def drawBoard(game):
    print('   |   |')
    print(' ' + game[0] + ' | ' + game[1] + ' | ' + game[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game[3] + ' | ' + game[4] + ' | ' + game[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game[6] + ' | ' + game[7] + ' | ' + game[8])
    print('   |   |')


### We keep a total count of plays made, starting with 1. If the total count divided by 2 has a remainder of 1, it means the current player is Player 1.
### If the total count divided by 2 has not remainder, it means the current player is Player 2. 
def playerNumber(playerNo):
    ## Write your code below
    ## You take in 1 input called playerNo, and output 2 numbers: 1 and 2

### First player's letter is "O" while second player's letter is "X" 
def playerLetter(num):
    ## Write your code below
    ## You take in 1 input called num, and output 2 letters: "O" or "X"


### Here we check if the spot that the Player picks is clearn, i.e. contains a spacebar " ".
def spotClear(spotPicked):
    return boardList[spotPicked] == " "


### Here we ask the Player to give us an input on which spot on the board they would like to play. While 
def playerMove():
    numbers = range(9)
    spot = input("Pick a spot by keying in a number between 0 to 8.\n")
    spot = int(spot)

    ## Write your code below
    ## You will need a while loop here as long as the input you get for spot is invalid. You need to check for 2 conditions here.
    ## (1) Input is not a number from 0 to 8
    ## (2) The spot that corresponds to the input is already taken


    return int(spot)
    
### Here we change the item in the list to the player's letter, which is either "O" or "X"
def markSpot():
    ## Write your code below
    ## You need to replace the spot indicated by the playerMove in the boardList list to the player's letter, i.e. "X" or "O"
    ## Tips: Do not specify "X" or "O" directly, take it instead from the function playerLetter(num), where you need to give playerLetter one input, which is the current player's letter
	boardList[playerMove()] = playerLetter(playerNum)


### This function checks all the combinations that would enable the player to win the game.
def hasWon(bo, le):
    if (
    (bo[0] == le and bo[1] == le and bo[2] == le) or # across the top
    (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
    (bo[6] == le and bo[7] == le and bo[8] == le) or # across the bottom
    (bo[0] == le and bo[3] == le and bo[6] == le) or # down the left side
    (bo[1] == le and bo[4] == le and bo[7] == le) or # down the middle
    (bo[2] == le and bo[5] == le and bo[8] == le) or # down the right side
    (bo[0] == le and bo[4] == le and bo[8] == le) or # diagonal
    (bo[2] == le and bo[4] == le and bo[6] == le)):# diagonal
        drawBoard(boardList)
        print "You have won!"
        return False
    else:
    	return True

## Check if the board has already been fully played, i.e. no more empty spots left
def boardIsFull():
    ## Tips: use a for loop combined with an if statement. This function needs to either return a True or a False


boardList = [" "] * 9

print "Welcome to Tic Tac Toe!"
	
playerNum = 1

runGame = True

while runGame == True:
    runGame = boardIsFull()
    guideBoard()
    print "It is Player " + str(playerNumber(playerNum)) + "\'s turn. The letter you play is " + playerLetter(playerNum)
    drawBoard(boardList)
    markSpot()
    runGame = hasWon(boardList, playerLetter(playerNum))
    playerNum += 1