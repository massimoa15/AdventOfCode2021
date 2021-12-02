with open('input.txt') as file:
    inputLines = file.readlines()

horizontal = 0
depth = 0

for inputLine in inputLines:
    [direction,value] = inputLine.split()
    value = int(value)
    if direction == "forward":
        horizontal += value
    elif direction == "up":
        depth -= value
    elif direction == "down":
        depth += value

print(depth * horizontal)