inf_ = int(1e9)
import heapq
T = int(input())
answer = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
for _ in range(T):
  n = int(input())
  table= [list(map(int,input().split())) for __ in range(n)]
  visited = [[inf_]*(n) for _i_ in range(n)]
  visited[0][0] = table[0][0]
  q = []
  heapq.heappush(q,(table[0][0],(0,0)))
  while q:
    cost, state = heapq.heappop(q)
    if visited[state[0]][state[1]]< cost:
      continue
    for j in range(4):
      nx = state[0] + dx[j]
      ny = state[1] + dy[j]
      #print(nx,ny)
      if 0<=nx<n and 0<=ny<n:
        dst = cost+ table[nx][ny]
        if visited[nx][ny]>dst:
          visited[nx][ny]=dst
          heapq.heappush(q,(dst,(nx,ny)))
  answer.append(visited[n-1][n-1])

for i in range(T):
  print(answer[i])
