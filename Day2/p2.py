with open('input.txt') as file:
    inputLines = file.readlines()

horizontal = 0
depth = 0
aim = 0

for inputLine in inputLines:
    [direction,value] = inputLine.split()
    value = int(value)
    if direction == "forward":
        horizontal += value
        depth += aim * value
    elif direction == "up":
        aim -= value
    elif direction == "down":
        aim += value

print(depth * horizontal)