with open('input.txt') as file:
#with open('example.txt') as file:
    input = file.readlines()

startFish = input[0].split(',')
startFish = list(map(int, startFish))

# This array will tell you how many fish exist with the value equal to their index number ie fish[0] will tell you how many fish with value 0 there are, fish[1] will tell you how many with value 1, etc.
fish = [0] * 9

# init fish with startFish values
for f in startFish:
    fish[f] += 1

numDays = 256

for i in range(0, numDays):
    #Now we need to shift all values of fish one to the left with 1 exception. For all fish[0] we shift them to fish[8] but also add them to fish[6]
    numReady = fish[0]
    for j in range(1, len(fish)):
        fish[j-1] = fish[j]
    # For every fish ready to spawn another we must create a fish with value 8 (represented by being at index 8) and also create a fish with value 6. we can shift the value to fish[8] but must add to fish[6] because fish[6] will include fish that were previously fish[7]
    fish[8] = numReady
    fish[6] += numReady

numFish = 0
for i in range(0, len(fish)):
    numFish += fish[i]
print(numFish)
    