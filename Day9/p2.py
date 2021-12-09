# Global variables
numRows = 0
numCols = 0

height9Val = -2 # This is the value that we initialize parts of the basinMap to if they have height 0 on the heightMap
numBasinCode = -3 # If returnNewBasinNumber returns -3 then we know we need to assign a new value

# This will update the basin (if needed) and return the new map
def updateBasinNumber(basinMap,x,y,numBasins):
    # First check if the value at x,y needs to be updated (is uninitialized aka == -1)
    if basinMap[y][x] == -1:
        # Check all adjacent squares. If any of them are assigned a value (>=0) then use that. If not, then give this the newest basin number (numBasins, then increment by 1)
        if x > 0 and basinMap[y][x-1] >= 0:
            basinMap[y][x] = basinMap[y][x-1]
        elif y > 0 and basinMap[y-1][x] >= 0:
            basinMap[y][x] = basinMap[y-1][x]
        elif x < numCols-1 and basinMap[y][x+1] >= 0:
            basinMap[y][x] = basinMap[y][x+1]
        elif y < numRows-1 and basinMap[y+1][x] >= 0:
            basinMap[y][x] = basinMap[y+1][x]
        else:
            # If you're here, then we need to assign it numBasins
            basinMap[y][x] = numBasins
            numBasins += 1

        # Now that we have determined the value of this square, call this function again for all adjacent ones
        if x > 0:
            [basinMap,numBasins] = updateBasinNumber(basinMap,x-1,y,numBasins)
        if y > 0:
            [basinMap,numBasins] = updateBasinNumber(basinMap,x,y-1,numBasins)
        if x < numCols-1:
            [basinMap,numBasins] = updateBasinNumber(basinMap,x+1,y,numBasins)
        if y < numRows-1:
            [basinMap,numBasins] = updateBasinNumber(basinMap,x,y+1,numBasins)

        # Done
        return [basinMap,numBasins]    

    # Not uninitialized, just return basinMap
    else:
        return [basinMap,numBasins]


with open('input.txt') as file:
#with open('example.txt') as file:
    inputLines = file.readlines()

heightMap = []

# inputLines is the whole input as a list of strings. Need to separate each line into a list of characters
for inputLine in inputLines:
    # Save the current line as a list of chars
    temp = list(inputLine.strip())
    # Convert the list of chars as a list of ints
    temp = list(map(int, temp))
    # Add this list of ints to the heightMap 2D list
    heightMap.append(temp)

# Get map dimensions
numRows = len(heightMap)
numCols = len(heightMap[0])

ans = 1

basinMap = [[-1 for i in range(numCols)] for j in range(numRows)]
# numBasins will count the number of basins that we have discovered and will also be used to number the basins as we go along
numBasins = 0

# initialize basinMap
for y in range(0,numRows):
    for x in range(0,numCols):
        if heightMap[y][x] == 9:
            # This is not part of any basin. Make it equal to -2 in basinMap
            basinMap[y][x] = height9Val

# Let's look at all basins and assign vals
for y in range(0,numRows):
  for x in range(0,numCols):
    temp = basinMap.copy()
    [temp2,numBasins] = updateBasinNumber(temp,x,y,numBasins)
    basinMap = temp2.copy()      

basinSizes = [0] * numBasins

# Look through all basinMap and calculate the sizes of each basin and add it to basinSizes
for i in range(0, numBasins):
    for y in range(0, numRows):
        for x in range(0, numCols):
            if basinMap[y][x] == i:
                basinSizes[i] += 1

# Let's take the top 3 values in basinSizes
for i in range(0,3):
    # Get the largest value
    temp = max(basinSizes)
    print(temp)
    # Remove largest value from list
    basinSizes.remove(temp)
    ans *= temp

print(ans)