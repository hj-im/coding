from collections import deque

N, M = map(int,input().split())
table = []
for _ in range(N):
    lst = list(map(int,input()))
    table.append(lst)
q = deque([])
q.append((0,0,1))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
table[0][0]=0
while q:
    x,y,cost = q.popleft()
    if x == N-1 and y == M-1:
        print(cost)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if table[nx][ny] == 1:
                table[nx][ny] = 0
                q.append((nx,ny,cost+1))

