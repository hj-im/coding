N = int(input())

table = [list(map(int,input().split())) for _ in range(N)]
minV = min(map(min, table))
maxV = max(map(max, table))


from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

ans = minV
for height in range(minV, maxV+1):
    visited = [[0] * N for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] >= height and visited[i][j] == 0:
                visited[i][j] = 1
                q = deque([(i,j)])
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<= nx< N and 0<= ny< N:
                            if visited[nx][ny] == 0 and table[nx][ny] >= height:
                                visited[nx][ny] = 1
                                q.append((nx, ny))
                tmp +=1
    ans = max(ans,tmp)
print(ans)