import statistics

def isOpener(c):
  openers = ['(','[','{','<']
  return c in openers

def isCloser(c):
  closers = [')',']','}','>']
  return c in closers

def isMatch(opener,closer):
  if opener == '(':
    return closer == ')'
  if opener == '[':
    return closer == ']'
  if opener == '{':
    return closer == '}'
  if opener == '<':
    return closer == '>'
  return False

def getCloser(c):
  if c == '(':
    return ')'
  if c == '[':
    return ']'
  if c == '{':
    return '}'
  if c == '<':
    return '>'
  return 0


with open('input.txt') as file:
#with open('example.txt') as file:
    inputLines = file.readlines()

stack = []
scores = []


for inputLine in inputLines:
  # Loop through all chars in this line
  for c in inputLine:
    # Opener read, add to stack
    if isOpener(c):
      stack.append(c)
    # Closer, pop stack and see if it's a match
    elif isCloser(c):
      if not isMatch(stack.pop(), c):
        # c is the corrupt char
        stack = []
        break
  # Here when done reading input this line. Now see what's left in the stack and add to ans
  stackSize = len(stack)
  temp = 0
  for i in range(0,stackSize):
    # First multiply ans by 5
    temp *= 5
    c = stack.pop()
    # See what c is and add to ans accordingly
    if c == '(':
      temp += 1
    if c == '[':
      temp += 2
    if c == '{':
      temp += 3
    if c == '<':
      temp += 4
  if temp == 0:
    continue
  # Done with stack, add temp to the scores list
  scores.append(temp)
     
#print(scores)
print(statistics.median(scores))
