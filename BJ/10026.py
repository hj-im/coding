from collections import deque
N = int(input())

table = [list(map(str, input())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = []
for s in range(2):
    visited = [[0]*N for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                q = deque()
                q.append((i, j))
                while q:
                    x,y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                        # 색약 아닌 사람
                            if s == 0:
                                if table[nx][ny] == table[x][y] and visited[nx][ny] == 0:
                                    visited[nx][ny] = 1
                                    q.append((nx,ny))
                        # 색약인 사람
                            else:
                                if table[nx][ny] in ['R', 'G'] and table[x][y] in ['R', 'G'] and visited[nx][ny] == 0:
                                    visited[nx][ny] = 1
                                    q.append((nx,ny))
                                elif table[nx][ny] =='B' and table[x][y] == 'B' and visited[nx][ny] == 0:
                                    visited[nx][ny] = 1
                                    q.append((nx,ny))
                tmp +=1
    ans.append(tmp)
for i in ans:
    print(i, end=' ')

