def calcFuelUsed(pos, goal):
    amt = 0
    dist = abs(pos-goal)
    for i in range(1, dist+1):
        amt += i
    return amt

import statistics

with open('input.txt') as file:
#with open('example.txt') as file:
    input = file.readlines()

positions = input[0].split(',')
positions = list(map(int, positions))

#We cannot use the median this time because we no longer have equal values of fuel use based on distance (no longer linear. Fuel cost increase is not the same as distance increase)
#Let's try the mean? Again, this is just a guess based on intuition. The mean worked for the example input but not for my input so I decided to also check the values + and - 1 compared to the mean. The lowest of these was the correct answer
goalPosition = round(statistics.mean(positions))

amtFuelUsed = [0,0,0]

# Let's check with this goal position (the mean) and also goalPosition+1 and -1
for position in positions:
    amtFuelUsed[0] += calcFuelUsed(position,goalPosition-1)
    amtFuelUsed[1] += calcFuelUsed(position,goalPosition)
    amtFuelUsed[2] += calcFuelUsed(position,goalPosition+1)

print(amtFuelUsed)

ans = min(amtFuelUsed)

print(ans)