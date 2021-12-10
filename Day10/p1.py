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

def getCorruptValue(c):
  if c == ')':
    return 3
  if c == ']':
    return 57
  if c == '}':
    return 1197
  if c == '>':
    return 25137
  return 0


with open('input.txt') as file:
#with open('example.txt') as file:
    inputLines = file.readlines()

stack = []
ans = 0

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
        ans += getCorruptValue(c)
        stack = []
        break
      
print(ans)
