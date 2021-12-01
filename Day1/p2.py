with open('input.txt') as file:
    inputLines = file.readlines()

# Convert from strings to ints
inputInts = [int(inputLine) for inputLine in inputLines]

numDeeper = 0

lastSum = inputInts[0] + inputInts[1] + inputInts[2]

# Start at 2 because that's the middle of the second window. End 1 from the end because we do i+1
for i in range(2, len(inputInts)-1):
    # Calculate sum of current window
    curSum = inputInts[i-1] + inputInts[i] + inputInts[i+1]
    if curSum > lastSum:
        numDeeper += 1
    # Overwrite lastSum now that we're moving to the next window
    lastSum = curSum

print(numDeeper)
