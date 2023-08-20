expression = input().strip()
stack = []
answer = ""
for e in expression:
  if e.isalpha():
    answer += e
  elif e == '*' or e == '/':
    while stack:
      if stack[-1] == '*' or stack[-1] == '/':
        answer += stack.pop()
      else:
        break
    stack.append(e)
  elif e == '+' or e == '-':
    while stack:
      if stack[-1] == '(':
        break
      answer += stack.pop()
    stack.append(e)
  elif e == '(':
    stack.append(e)
  elif e == ')':
    while stack:
      if stack[-1] == '(':
        stack.pop()
        break
      answer += stack.pop()

while stack:
  answer += stack.pop()

print(answer)