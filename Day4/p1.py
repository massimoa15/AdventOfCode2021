# Functions
def checkWinningBoard(board):
    return checkWinningRows(board) or checkWinningCols(board)


def checkWinningRows(board):
    # Loop through all rows in board and return true if one of them consists of all winning characters: '*'
    for row in board:
        if row.count('*') == len(row):
            return True
    # Here if none of the rows are winning
    return False

def checkWinningCols(board):
    for colNum in range(0,len(board)):
        tempList = []
        # Now we need to go through each row and append the value for the current column
        for rowNum in range(0,len(board)):
            tempList.append(board[rowNum][colNum])
        # Now we have the current column. Let's check if it's a winner
        if checkWinningCol(tempList) is True:
            return True
        # Not a winner. Try with the next column
    #No columns are winners. No winning columns
    return False

def checkWinningCol(col):
    return col.count('*') == len(col)

def boardContainsVal(board, val):
    for row in board:
        if val in row:
            return True
    # No row contains this value
    return False

def replaceNumInBoard(board, num):
    for row in board:
        if num in row:
            i = row.index(num)
            row[i] = '*'
            break

def callNums(boards, drawOrder):
    for numberCalled in drawOrder:
        # Need to replace every occurrence with this number in all boards with '*' and then check if they are winners
        for board in boards:
            if boardContainsVal(board, numberCalled):
                replaceNumInBoard(board, numberCalled)
                if checkWinningBoard(board):
                    # Calculate the info we need and return it
                    sum = calcSum(board)
                    ans = sum * int(numberCalled)
                    return ans

# Calculates the sum of all numbers on this board that weren't called
def calcSum(board):
    sum = 0
    for row in range (0, len(board)):
        for col in range(0, len(board)):
            if board[row][col] != '*':
                sum += int(board[row][col])
    return sum

# Start of main function
with open('input.txt') as file:
    # file.read will read the entire input and return it (as one string). Using split() will allow us to create a list of input where you separate each item by 2 newlines, since that is how the input file is written
    input = file.read().split('\n\n')

boardSize = 5

# This is a list of numbers in the order they are drawn. We know that it's the first input from the text file and they're delimited by commas, so we are splitting the first value by commas 
drawOrder = input[0].split(',')
# Take the input and make a sublist from index 1 onward. This will have each board as 1 string.
boardsRaw = input[1:]

# This will count what the current board number we are on is for writing to the new list of boards
boardNum = 0

# This will have the 3 dimensional list of boards
boards = []

# We need to take each board in boardsRaw and convert each value into a 2d list where each number is its own index. 
# This will be a 3D list where the first index is the board number, the second index is the row number, and the third index is the column number
for boardRaw in boardsRaw:
    # Separate the list into individual rows
    rawRows = boardRaw.split('\n')

    tempBoard = [["-1" for i in range(boardSize)] for j in range(boardSize)]

    rowNum = 0
    for rawRow in rawRows:
        rowVals = rawRow.split(' ')
        # Need to remove any empty entries because 1 digit numbers will have 2 spaces.
        while '' in rowVals:
            rowVals.remove('')
        # Now we need to add these values to the current boardNum

        tempBoard[rowNum] = rowVals
        rowNum += 1
    # Now we have the current board stored in tempBoard. Save it in our list boards[]
    boards.append(tempBoard)
    boardNum += 1

print('answer: ',callNums(boards, drawOrder))
