from collections import deque

N, K = map(int, input().split())
dq = deque([N])
time = [-1] * 100001
time[N] = 0

while dq:
  now = dq.popleft()
  if now == K:
    print(time[now])
    break
  for next in [now-1, now+1, 2*now]:
    if 0 <= next <= 100000 and time[next] == -1:
      if next == 2*now:
        time[next] = time[now]
        dq.appendleft(next)
      else:
        time[next] = time[now] + 1
        dq.append(next)