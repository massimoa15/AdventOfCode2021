with open('input.txt') as file:
    inputLines = file.readlines()
# Number of lines that were read
numLines = len(inputLines)

#make copies of both lists as we will be removing values as we do calculations
oxygenList = co2List = inputLines
# Counters
numOxygenLines = numCO2Lines = numLines

# Need to subtract 1 because it is counting the newline character 
numDigits = int(len(inputLines[0])) - 1

#Number of times the bit 1 appears in the current column
numOnesInCol = 0

#Oxygen calculations
for digNum in range(0, numDigits):
  if numOxygenLines == 1:
    break
  # Reset counter
  numOnesInCol = 0
  for oxygenNum in oxygenList:
    if oxygenNum[digNum] == "1":
      numOnesInCol += 1
  # Now we can determine the most common bit by seeing if numOnesInCol > numOxygenLines/2
  prominentBit = "0"

  if numOnesInCol >= numOxygenLines/2: #If this doesn't work then we should count num of 1s and num of 0s
    prominentBit = "1"
  
  #Need to work with a second list so we don't skip anything when we remove items from list
  oxygenList2 = []
  numOxygenLines2 = 0

  # Check all values in oxygenList and add the ones that have this bit to the new list
  for oxygenNum in oxygenList:
    if oxygenNum[digNum] == prominentBit:
      oxygenList2.append(oxygenNum)
      numOxygenLines2 += 1
  
  #Overwrite values with the temp values we were using
  oxygenList = oxygenList2
  numOxygenLines = numOxygenLines2

  #print("List reduced to ", numOxygenLines, " entries. The most common bit was ", prominentBit)

for digNum in range(0, numDigits):
  if numCO2Lines == 1:
    break
  #Reset counter
  numOnesInCol = 0
  for co2Num in co2List:
    if co2Num[digNum] == "1":
      numOnesInCol += 1
  #Now we can determine the prominent bit
  prominentBit = "0"
  
  if numOnesInCol >= numCO2Lines/2:
    prominentBit = "1"

  #This is the temp list so we don't skip anything
  co2List2 = []
  numCO2Lines2 = 0

  #Check all values in co2List and add the ones to the temp list that have the correct bit
  for co2Num in co2List:
    if co2Num[digNum] != prominentBit:
      co2List2.append(co2Num)
      numCO2Lines2 += 1

  #overwrite values with temp values
  co2List = co2List2
  numCO2Lines = numCO2Lines2
    

# Now convert to decimal and print product
oxygenVal = int(oxygenList[0], 2)
co2Val = int(co2List[0], 2)
print(oxygenVal * co2Val)