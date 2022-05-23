# 11 뱀
n = int(input())
k = int(input())

# row col
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
direction = [list(map(str, input().split())) for _ in range(l)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dic = {}
for i in direction:
    dic.update({i[0]: i[1]})

graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in apple:
    graph[i[0]][i[1]] = 1

start = (1, 1)
dir = 0
# for x,c in direction:
graph[1][1] = 2
q = []
q.append(start)
cnt = 0
while True:
    x, y = start
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 1 or nx > n or ny < 1 or ny > n or graph[nx][ny] == 2:
        cnt += 1
        break
    if graph[nx][ny] == 1:
        q.append((nx, ny))
        graph[nx][ny] = 2
    else:
        q.append((nx, ny))
        tx, ty = q.pop(0)
        graph[nx][ny] = 2
        graph[tx][ty] = 0

    start = (nx, ny)
    cnt += 1
    if str(cnt) in dic.keys():
        # print('123')
        d = dic[str(cnt)]
        if d == 'L':
            dir = dir - 1 if dir > 0 else 3
        else:
            dir = dir + 1 if dir < 3 else 0

print(cnt)