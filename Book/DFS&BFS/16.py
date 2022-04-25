n, m = map(int, input().split())
from collections import deque

graph_init = [list(map(int, input().split())) for _ in range(n)]
from itertools import combinations
import copy

virus = []
possible = []
wall = []
for i in range(n):
    for j in range(m):
        if graph_init[i][j] == 2:
            virus.append([i, j])
        elif graph_init[i][j] == 0:
            possible.append([i, j])

q = deque(virus)

max_ans = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for candidate in combinations(possible, 3):
    graph = [item[:] for item in graph_init]
    init_cost = len(possible) - 3
    for cx, cy in candidate:
        graph[cx][cy] = 1
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    q.append([nx, ny])
                    graph[nx][ny] = 2
                    init_cost -= 1
    max_ans = max(init_cost, max_ans)
print(max_ans)