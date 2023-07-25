import sys
input = sys.stdin.readline

strings = []
while True:
  string = input().replace("\n", "")
  if string == ".":
    break
  strings.append(string)
    
for string in strings:
  stack = []
  
  for s in string:
    if s == "(" or s == "[":
      stack.append(s)
    elif s == ")":
      if len(stack) > 0 and stack[-1] == "(":
        stack.pop()
      else:
        stack.append(s)
    elif s == "]":
      if len(stack) > 0 and stack[-1] == "[":
        stack.pop()
      else:
        stack.append(s)

  if len(stack) == 0:
    print("yes")
  else:
    print("no")