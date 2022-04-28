from collections import deque
M, N, K = map(int,input().split())
table = [[0]*N for _ in range(M)]


lst = []
for _ in range(K):
    lbx, lby, rax, ray = map(int,input().split())
    for i in range(lby, ray):
        for j in range(lbx,rax):
            table[i][j] = 1
dx = [1,0,0,-1]
dy = [0,-1,1,0]
table0 = [item[:] for item in table]
ans = []
for i in range(M):
    for j in range(N):
      if table0[i][j] == 0:
        table0[i][j] =1
        cnt = 1
        q = deque([])
        q.append([i, j])
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<M and 0<=ny<N:
                  if table0[nx][ny] == 0:
                      q.append([nx, ny])
                      table0[nx][ny] =1
                      cnt+=1
        ans.append(cnt)

ans.sort()
print(len(ans))
for x in ans:
  print(x)