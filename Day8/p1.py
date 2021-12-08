with open('input.txt') as file:
#with open('example.txt') as file:
    inputLines = file.readlines()

ans = 0

for inputLine in inputLines:
    # Separate the input into the input and output half
    input,output = inputLine.split("|")
    #Now we take the output and count how many of the values are 1 4 7 or 8. We can do this by checking if the lengths are 2, 4, 3, or 7 as these numbers are the only ones with these lengths
    outputVals = output.strip().split(" ") #separate into a list
    for val in outputVals:
        if len(val) == 2 or len(val) == 4 or len(val) == 3 or len(val) == 7:
            ans += 1

print(ans)