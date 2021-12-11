def flash(grid,y,x,numFlashes,flashTracker):
    flashTracker[y][x] = True
    numFlashes += 1
    # Need to increment all adjacent values and flash those if their new value after incrementing is a 10 (if it's >10 then it's already flashed)

    # Let's check that y isn't on the top row. If y > 0 then we can check the 3 locations above this [y][x] position
    if y > 0:
        # Grid is also not first column, can do up and to the left
        if x > 0:
            grid[y-1][x-1] += 1
            if grid[y-1][x-1] >= 10 and not flashTracker[y-1][x-1]:
                [grid,numFlashes,flashTracker] = flash(grid,y-1,x-1,numFlashes,flashTracker)
        grid[y-1][x] += 1
        if grid[y-1][x] >= 10 and not flashTracker[y-1][x]:
            [grid,numFlashes,flashTracker] = flash(grid,y-1,x,numFlashes,flashTracker)
        if x < numCols - 1:
            grid[y-1][x+1] += 1
            if grid[y-1][x+1] >= 10 and not flashTracker[y-1][x+1]:
                [grid,numFlashes,flashTracker] = flash(grid,y-1,x+1,numFlashes,flashTracker)
    # Now check to the left and right
    if x > 0:
        grid[y][x-1] += 1
        if grid[y][x-1] >= 10 and not flashTracker[y][x-1]:
            [grid,numFlashes,flashTracker] = flash(grid,y,x-1,numFlashes,flashTracker)
    if x < numCols-1:
        grid[y][x+1] += 1
        if grid[y][x+1] >= 10 and not flashTracker[y][x+1]:
            [grid,numFlashes,flashTracker] = flash(grid,y,x+1,numFlashes,flashTracker)
    # Now check below the current location
    if y < numRows-1:
        if x > 0:
            grid[y+1][x-1] += 1
            if grid[y+1][x-1] >= 10 and not flashTracker[y+1][x-1]:
                [grid,numFlashes,flashTracker] = flash(grid,y+1,x-1,numFlashes,flashTracker)
        grid[y+1][x] += 1
        if grid[y+1][x] >= 10 and not flashTracker[y+1][x]:
            [grid,numFlashes,flashTracker] = flash(grid,y+1,x,numFlashes,flashTracker)
        if x < numCols - 1:
            grid[y+1][x+1] += 1
            if grid[y+1][x+1] >= 10 and not flashTracker[y+1][x+1]:
                [grid,numFlashes,flashTracker] = flash(grid,y+1,x+1,numFlashes,flashTracker)
    # Checked all possibilities, return values
    return [grid,numFlashes,flashTracker]

with open('input.txt') as file:
#with open('example.txt') as file:
    inputLines = file.readlines()

grid = []

# Convert this into a list of lists, then convert to an int list of lists
for inputLine in inputLines:
    grid.append(list(map(int,inputLine.strip())))

# Now grid has the 2D list that we will be working with (all ints)
global numRows
numRows = len(grid)
global numCols
numCols = len(grid[0])

numDays = 100

numFlashes = 0

flashTracker = [[False for i in range(numCols)] for j in range(numRows)]

for day in range(0,numDays):
    # Reset the flash tracker, no one has flashed this day yet
    for y in range(0,numRows):
        for x in range(0,numCols):
            flashTracker[y][x] = False

    # First we increase the energy level of all octo by 1
    for y in range(0,numRows):
        for x in range(0,numCols):
            grid[y][x] += 1

    # Then any octo with an energy level of >9 will flash, increasing the energy level of all adjacent octo (including diagonal) by 1. This can have a chain reaction but all octo can only flash once per day
    for y in range(0,numRows):
        for x in range(0,numCols):
            if grid[y][x] >= 10 and not flashTracker[y][x]:
                [grid,numFlashes,flashTracker] = flash(grid,y,x,numFlashes,flashTracker)

    # Now, reset any energy level >9 back down to 0
    for y in range(0,numRows):
        for x in range(0,numCols):
            if grid[y][x] > 9:
                grid[y][x] = 0

print(numFlashes)