from collections import deque
n,k =map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(n)]
s,cx,cy = map(int,input().split())
virus = []
possible = []
for i in range(n):
    for j in range(n):
        if lst[i][j] != 0:
            virus.append([lst[i][j], i, j, 0])
virus.sort()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque(virus)

lst2 = [item[:] for item in lst]
while q:
    value, x, y, t = q.popleft()
    if t == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not lst2[nx][ny]:
                lst2[nx][ny] = value
                q.append([value,nx,ny,t+1])
print(lst2[cx-1][cy-1])
