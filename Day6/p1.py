with open('input.txt') as file:
#with open('example.txt') as file:
    input = file.readlines()

fish = input[0].split(',')
fish = list(map(int, fish))

# Now fish is a list of all fish as ints

numDays = 80

for i in range(0, numDays+1):
    # Loop through every fish and decrease the number if you can. If the number is 0 then add a new fish with value 8 to the end
    numFish = len(fish)
    for j in range(0, numFish):
        if fish[j] == 0:
            fish[j] = 6
            fish.append(8)
        else:
            fish[j] -= 1

print(numFish)
    