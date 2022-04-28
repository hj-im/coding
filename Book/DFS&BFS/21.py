from collections import deque

n, l, r = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 2000

while cnt > 0:
    flag = 1
    check = set()
    all_visited = []

    for i in range(n):
        for j in range(n):
            if (i, j) not in check:
                q = deque()
                q.append((i, j))
                visited = []
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if l <= abs(board[nx][ny]-board[x][y]) <= r and (nx, ny) not in visited \
                                    and (nx, ny) not in all_visited:
                                q.append((nx,ny))
                                visited.append((nx,ny))
                                flag = 0
                visited = set(visited)
                if visited:
                    all_visited.append([item[:] for item in visited])
                check = set.union(check, visited)

    if flag:
        break

    for union in all_visited:
        u_len = len(union)
        power = 0
        for x, y in union:
            power += board[x][y]
        power = power//u_len
        for x, y in union:
            board[x][y] = power

    cnt -= 1

print(2000-cnt)

