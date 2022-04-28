from collections import deque
N = int(input())
table = [list(map(int,input())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [item[:] for item in table]
ans = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            visited[i][j] = 0
            tmp = 0
            q = deque()
            q.append((i,j))
            while q:
                x, y= q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if visited[nx][ny] == 1:
                            visited[nx][ny] = 0
                            q.append((nx,ny))
                            tmp+=1
            ans.append(tmp)

print(len(ans))
ans.sort()
for i in ans:
    print(i+1)