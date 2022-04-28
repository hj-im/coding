T = int(input())
dx = [-1,0,0,1]
dy = [0,1,-1,0]
from collections import deque

for __ in range(T):
    M, N, K  = map(int, input().split())
    ans = []
    table = [[0]*M for _ in range(N)]
    for _ in range(K):
        a,b = map(int,input().split())
        table[b][a] = 1

    for i in range(N):
        for j in range(M):
            if table[i][j] == 1:
                table[i][j] = 0
                q = deque([])
                q.append((i, j))
                cnt = 1
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M:
                            if table[nx][ny] == 1:
                                table[nx][ny] = 0
                                q.append((nx, ny))
                ans.append(cnt)
    print(len(ans))