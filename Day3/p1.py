with open('input.txt') as file:
    inputLines = file.readlines()
# Number of lines that were read
numLines = len(inputLines)

# Need to subtract 1 because it is counting the newline character 
numDigits = int(len(inputLines[0])) - 1

# This will store the number of 1s that appear in each column
bitCounter = []

for i in range(0, numDigits):
  bitCounter.append(0)

# Loop through all lines and count the 1's
for inputLine in inputLines:
  for i in range(0, numDigits):
    if inputLine[i] == "1":
      bitCounter[i] += 1

#Now check the values of bitCounter and if they are > numLines / 2 then we include a 1, else we include a 0
gammaRate = ""
epsilonRate = ""
for i in range(0, numDigits):
  if bitCounter[i] > numLines/2:
    gammaRate += "1"
    epsilonRate += "0"
  else:
    gammaRate += "0"
    epsilonRate += "1"
gammaRate = int(gammaRate, 2)
epsilonRate = int(epsilonRate, 2)

print(gammaRate * epsilonRate)
