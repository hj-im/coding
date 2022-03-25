from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
shark = []
N = int(input())
lst= []
for _ in range(N):
  lst.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if lst[i][j] == 9:
            shark = (2,i,j)
            lst[i][j] = 0

cnt = 0

# bfs
def bfs(shark,cnt, stack):
  q= deque()
  q.append([shark[1],shark[2]])
  visited = [[-1]*N for _ in range(N)]
  visited[shark[1]][shark[2]] = cnt
  eatLst = []
  while q:
    qlen = len(q)
    while qlen:
      x,y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx <N and 0<=ny < N:
          if visited[nx][ny] == -1:
            if lst[nx][ny] == 0 or lst[nx][ny] == shark[0]:
              # print('1',shark[0])
              q.append([nx,ny])
              visited[nx][ny] = visited[x][y] + 1
            elif 0 < lst[nx][ny] < shark[0]:
              # print('2',shark[0])
              eatLst.append([nx, ny])
      qlen -=1
      
    if eatLst:
       # print(eatLst)
       min_x,min_y = min(eatLst)
       stack.append([lst[min_x][min_y],min_x,min_y])
       if len(stack) == shark[0]:
         stack = []
         shark = (shark[0]+1,min_x,min_y)
       else:
         shark = (shark[0],min_x,min_y)
       lst[min_x][min_y] = 0
       v = visited[0:][0:]
       cnt =  v[x][y]+1
       return shark, cnt, stack
  return -1,-1,-1
stack = []
while True:
  
  shark, cnt, stack = bfs(shark, cnt, stack)
  if shark == -1 and cnt == -1 and stack == -1:
    break
