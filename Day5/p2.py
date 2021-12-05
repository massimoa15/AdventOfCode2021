def increasePos(diagramVal):
    if diagramVal == '.':
        return 1
    else: #Not a period, it's a number so just increment
        return diagramVal + 1


import re

with open('input.txt') as file:
#with open('example.txt') as file:
    inputLines = file.readlines()
# Input now has the whole input as a list

#numbers = re.findall('[0-9]+', str(inputLines))
xVals = re.findall('\d+,', str(inputLines))
yVals = re.findall(',\d+', str(inputLines))

#Remove commas from xVals and yVals
for x in range(0,len(xVals)):
    xVals[x] = int(xVals[x].replace(',',''))
for y in range(0,len(yVals)):
    yVals[y] = int(yVals[y].replace(',',''))

#Get the max values to determine the 2D list size
maxX = max(xVals)
maxY = max(yVals)

diagram = [["." for i in range(maxX+1)] for j in range(maxY+1)]

for inputLine in inputLines:
    [startPos, endPos] = inputLine.strip().split(' -> ')
    [startX, startY] = startPos.split(',')
    [endX, endY] = endPos.split(',')
    startX,startY,endX,endY = int(startX),int(startY),int(endX),int(endY)

    #Now check if the x value changed or if the y value changed
    if startY == endY:
        if startX < endX:
            for x in range(startX,endX+1):
                #Arbitrarily using startY as the y position since only either the x or y value is changing (no diagonal)
                diagram[startY][x] = increasePos(diagram[startY][x])
        elif startX > endX:
            for x in range(endX, startX+1):
                diagram[startY][x] = increasePos(diagram[startY][x])
    # Y value changed
    elif startX == endX:
        if startY < endY:
            for y in range(startY, endY+1):
                diagram[y][startX] = increasePos(diagram[y][startX])
        elif startY > endY:
            for y in range(endY, startY+1):
                diagram[y][startX] = increasePos(diagram[y][startX])
    # Both values are changing, this is a diagonal line
    else:
        yInc = 1
        #With this, we will be able to always increment x and will know whether we need ot increment or decrement y
        if startX < endX:
            x1 = startX
            x2 = endX
            y1 = startY
            y2 = endY
            # This means that the y value is moving in the opposite direction of the x value so we decrement instead of increment. In this case we are increasing in th X and decreasing in the Y
            if startY > endY:
                yInc = -1
        else:
            x1 = endX
            x2 = startX
            y1 = endY
            y2 = endY
            # This means that the y value is moving in the opposite direction of the x value so we decrement instead of increment. In this case we are decreasing in the X and increasing in the Y (but it is inverted)
            if startY < endY:
                yInc = -1
        # Now increment x from x1 to x2 and y from y1 to y2 and update map
        x,y = x1,y1
        while x <= x2:
            diagram[y][x] = increasePos(diagram[y][x])
            x += 1
            y += yInc


numOverlaps = 0
#We are done writing to diagram. Count number of values 2+
for row in diagram:
    numOverlaps += len(re.findall('[2-9]\d*',str(row)))

print(numOverlaps)
