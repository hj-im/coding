from collections import deque
def bfs(info,graph):
    # 0 == sheep, 1 == wolf
    answer = 0
    q = deque([([0],1,0)])
    while q:
        indices, sheep, wolf = q.popleft()
        answer = max(answer, sheep)
        for index in indices:
            for child in graph[index]:
                sheep_count, wolf_count = sheep, wolf
                if child not in indices:
                    if info[child] == 0:
                        sheep_count += 1
                    else:
                        wolf_count += 1
                    if sheep_count > wolf_count:
                        q.append([indices + [child], sheep_count, wolf_count])
    return answer

def func(edges,length):
    graph = [[] for i in range(length)]
    for _edge_ in edges:
        parent, child = _edge_
        graph[parent].append(child)
    return graph
    
            
def solution(info, edges):
    graph = func(edges,len(info))
    answer = bfs(info, graph)
    # answer = 1
    return answer
