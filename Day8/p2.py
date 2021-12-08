def doesAContainB(a,b):
    # Loop through all values of b and see if they're in a. If any of them aren't then return false. If you get through all of B then return true
    for i in range(0,len(b)):
        if b[i] not in a:
            return False
    return True
# This will return the number of letters that appear in b that also appear in a
def numberOfSameLetters(a,b):
    count = 0
    for i in range(0,len(b)):
        if b[i] in a:
            count += 1
    return count

def lettersToNum(numbersAsLetters, str):
    for i in range(0, len(numbersAsLetters)):
        if str == numbersAsLetters[i]:
            return i
    return -1

with open('input.txt') as file:
#with open('example.txt') as file:
    inputLines = file.readlines()

# We need to keep track of each of the 7 segments and determine which letter corresponds to each
# We will assume all segments can be all values to start. If any segment can no longer be that letter then we will remove it. Do this until all segments are length 1
segments = ['abcdefg'] * 7

# segments [0] will be the segment corresponding to a, [1] corresponds to b, and so on.
# This is what an 8 would look like in the correct order
#  aaaa      0000
# b    c    1    2
# b    c    1    2
#  dddd      3333
# e    f    4    5
# e    f    4    5
#  gggg      6666

# Sum of answers
ans = 0

inputValsOrig = []
outputValsOrig = []

inputVals = []
outputVals = []

for inputLine in inputLines:
    # Separate the input into the input and output halves
    input,output = inputLine.split("|")

    outputValsOrig.append(output.strip().split(" ")) #separate into a list
    inputValsOrig.append(input.strip().split(" "))

# Let's sort all the inputVals and outputVals alphabetically. Loop through all values of inputValsOrig and sort each value of each sublist
for lineNum in range(0, len(inputValsOrig)):
    tempAns = []
    for i in range(0, len(inputValsOrig[lineNum])):
        # Now, we need to sort inputValsOrig[lineNum][i] alphabetically
        tempAns.append("".join(sorted(inputValsOrig[lineNum][i])))
    inputVals.append(tempAns)

for lineNum in range(0, len(outputValsOrig)):
    tempAns = []
    for i in range(0, len(outputValsOrig[lineNum])):
        # Now, we need to sort inputValsOrig[lineNum][i] alphabetically
        tempAns.append("".join(sorted(outputValsOrig[lineNum][i])))
    outputVals.append(tempAns)


#Now we have sorted every string in the file alphabetically so we know they're always in the same order. Loop through each line and determine the output number
for rowNum in range(0, len(inputVals)):
    # numbersAsLetters will tell you what each number is written as in letter form.
    numbersAsLetters = [''] * 10

    inputVal = inputVals[rowNum]
    # We can sort each line of input by length so that we know which length appears at which indexes
    inputVal = sorted(inputVal,key=len)
    # By sorting the list by length, we know we are determining which values are the numbers 1,7, and 4 as they are the shortest lengths. In fact, we can say the following
    numbersAsLetters[1] = inputVal[0]
    numbersAsLetters[7] = inputVal[1]
    numbersAsLetters[4] = inputVal[2]
    numbersAsLetters[8] = inputVal[9]

    # Now we can loop through inputVal from index [3,8] inclusive
    for i in range(3, 9):
        # Let's determine length 5 guys (numbers 2,3,5)
        if len(inputVal[i]) == 5:
            # 3 is the only one that contains all of 7
            if(doesAContainB(inputVal[i],numbersAsLetters[7])):
                numbersAsLetters[3] = inputVal[i]
            # We also can look at the number of similar letters in length 5 inputs as the letters for 4. If the number does not contain all of 7 then we are looking at numbers 2 and 5. 2 uses 2 of the same segments as 4 and 5 uses 3 of the same segments
            elif(numberOfSameLetters(inputVal[i],numbersAsLetters[4])) == 2:
                numbersAsLetters[2] = inputVal[i]
            # The number of same letters isn't 2, then inputVal[i] must be a 5 because it has 3 of the same letters
            else:
                numbersAsLetters[5] = inputVal[i]        
        # Let's determine length 6 guys (numbers 0,6,9)
        if len(inputVal[i]) == 6:
            # 9 is the only one that contains all of 4
            if doesAContainB(inputVal[i],numbersAsLetters[4]):
                numbersAsLetters[9] = inputVal[i]
            # 6 contains all of 5, but 0 doesn't. So we can use that to determine which is which
            elif doesAContainB(inputVal[i],numbersAsLetters[5]):
                numbersAsLetters[6] = inputVal[i]
            # Not a 6, has to be a 0
            else:
                numbersAsLetters[0] = inputVal[i]
    
    # Now that we know what each number is as it's relative letter input, look at the output values and determine what the numbers are
    outputVal = outputVals[rowNum]
    tempAns = []
    for j in range(0, len(outputVal)):
        # Look at all output values and determine what number it is
        tempAns.append(lettersToNum(numbersAsLetters, outputVal[j]))

    # Need to convert temp to a real number. Let's convert it to a list of strings, then to 1 string, then to 1 int
    tempAns = ''.join(map(str,tempAns))
    tempAns = int(tempAns)
    ans += tempAns

print(ans)