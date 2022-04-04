import heapq
start = 1
INF = int(1e9)
visited = [INF]*(n+1)
graph= [[] * (n+1) for _ in range(n+1)]
for i in range(len(lst)):
  graph[lst[i][0]].append(lst[i][1])
  graph[lst[i][1]].append(lst[i][0])
start = 1
heapq.heappush(q,(0,start))
visited[1] = 0
while q:
  cost,start = heapq.heappop(q)
  if visited[start] < cost:
    continue
  if graph[start]:
    for s in graph[start]:
          n_cost = cost+1
          if n_cost< visited[s]:
            visited[s] = n_cost
            heapq.heappush(q,(n_cost,s))

min_dist = max(visited[1:])
cnt = visited.count(min_dist)
for i in range(len(visited)):
  if visited[i] == min_dist:
    k = i
    break
print(i,min_dist,cnt)
