# Global variables
numRows = 0
numCols = 0

def isLowestLocal(heightMap, x, y):
    val = heightMap[y][x]
    # Check if val above is less (need to make sure that there exists a value above)
    if(y > 0):
        # Has a value above [x][y] so check if it's less than map[y][x]
        if(heightMap[y-1][x] <= val):
            return False
    # Check lower value
    if(y < numRows-1):
        if(heightMap[y+1][x] <= val):
            return False
    if(x > 0):
        if(heightMap[y][x-1] <= val):
            return False
    if(x < numCols-1):
        if(heightMap[y][x+1] <= val):
            return False
    return True

with open('input.txt') as file:
#with open('example.txt') as file:
    inputLines = file.readlines()

heightMap = []

# inputLines is the whole input as a list of strings. Need to separate each line into a list of characters
for inputLine in inputLines:
    temp = list(inputLine.strip())
    temp = list(map(int, temp))
    heightMap.append(temp)


numRows = len(heightMap)
numCols = len(heightMap[0])

ans = 0

for y in range(0,numRows):
    for x in range(0,numCols):
        if isLowestLocal(heightMap,x,y):
            ans += heightMap[y][x]+1

print(ans)