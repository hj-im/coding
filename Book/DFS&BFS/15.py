from collections import deque
n, m, k, x = map(int, input().split())

lst = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    lst[a-1].append(b-1)

q = deque()
q.append([0,x-1])

visited = [0] * n
visited[x-1]=1
clst = []
while q:
    cost, position = q.popleft()
    if cost == k:
        clst.append(position)
    for next in lst[position]:
        if not visited[next]:
            visited[next] = 1
            q.append([cost+1,next])

if clst:
    clst.sort()
    for i in clst:
        print(i+1)
else:
    print(-1)