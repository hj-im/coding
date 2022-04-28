from collections import deque

M, N = map(int, input().split())
# M col N row
table = []
for i in range(N):
    table.append(list(map(int,input().split())))

well =[]
nowell = []
noto = []

for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            well.append([i,j])
        elif table[i][j] == -1:
            noto.append([i,j])
dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque(well)

visited = [[0]*M for _ in range(N)]

for l in well:
    visited[l[0]][l[1]] = 1
for l in noto:
    visited[l[0]][l[1]] = -1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]+1
                q.append([nx,ny])

check = M*N - len(noto)
maxV= 0
flag= 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            flag = 1
        maxV = max(maxV, visited[i][j])
if flag:
    print(-1)
elif maxV==1:
    print(0)
else:
    print(maxV-1)

