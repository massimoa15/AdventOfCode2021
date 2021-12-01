with open('input.txt') as file:
    inputLines = file.readlines()

# Convert from strings to ints
inputInts = [int(inputLine) for inputLine in inputLines]

numDeeper = 0

# Now loop through all values in inputLines and compare with the previous. If current > previous then increment the counter
for i in range(1, len(inputInts)):
    if inputInts[i] > inputInts[i-1]:
        numDeeper += 1

print(numDeeper)
