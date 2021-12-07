import statistics

with open('input.txt') as file:
#with open('example.txt') as file:
    input = file.readlines()

positions = input[0].split(',')
positions = list(map(int, positions))

# We use the median becaues it is the number that exists in the middle of all numbers in the list. The middle of all numbers would be the value with the least distance. 
# This was a guess not based in much except intuition and it gave me the correct answer for the example so I decided to also try it on my input and it worked
goalPosition = statistics.median(positions)

amtFuelUsed = 0

# Now loop through all values in positions and see the difference between the horizontal position
for position in positions:
    amtFuelUsed += abs(goalPosition - position)

print(amtFuelUsed)