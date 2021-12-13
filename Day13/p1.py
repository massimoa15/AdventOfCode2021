with open('input.txt') as file:
#with open('example.txt') as file:
    fullInput = file.read().split('\n\n')

# Now separate fullInput into the coordinates and the folding instructions
coordinateInput = fullInput[0].split('\n')
foldingInput = fullInput[1].split('\n')

# Let's find the highest x and y value in the coordinateInput
numRows = 0
numCols = 0

coordinates = []

for row in coordinateInput:
  x,y = list(map(int,row.strip().split(',')))
  if x > numCols:
    numCols = x
  if y > numRows:
    numRows = y
  coordinates.append([x,y])

# Now we have read all input. Need to increment numCols and numRows since we start reading at value 0
numCols += 1
numRows += 1

# Let's start by adding the coordinate input into the map which will represent the transparency paper
map = [['.' for i in range(0,numCols)] for j in range(0,numRows)]

# Now we have the map, replace all '.' with '#' to denote a dot being marked
for row in coordinates:
  map[row[1]][row[0]] = '#'

# Now we need to do all the fold rules and write a '#' anywhere there is a new overlap. Start by getting rid of the "fold along " at the start of each string
for i in range(len(foldingInput)):
  foldingInput[i] = foldingInput[i][11:]

# Now go through each input line and fold depending on where it is said to be folded
for i in range(len(foldingInput)):
  axis = foldingInput[i][0]
  val = int(foldingInput[i][2:])
  tempMap = []

  # Folding appears perp to y axis (at y = val)
  if axis == 'y':
    for y in range(val+1,numRows):
      for x in range(0,numCols):
        if map[y][x] == '#':
          diff = y-val
          map[val-diff][x] = '#'
    tempMap = map[:val]
    # Need to also update the number of rows.
    numRows = val

  # Folding appears perp to x axis (at x = val). Fold left (Keep values left of val, copy values on right over to the values on the left, mirrored)
  else:
    # Init tempMap to size of folded new map
    tempMap = [['.' for tempY in range(val)] for tempX in range(numRows)]
    for y in range(0,numRows):
      for x in range(val+1,numCols):
        if map[y][x] == '#':
          diff = x-val
          map[y][val-diff] = '#'
    
    # Copy tempMap over
    for y in range(0,numRows):
      for x in range(0,val):
        tempMap[y][x] = map[y][x]
    numCols = val
    

  # We break because we are only asked to do 1 fold for p1
  map = tempMap
  break

# Determine number of dots that are on the paper
numDots = 0
for row in map:
  numDots += row.count('#')

print(numDots)