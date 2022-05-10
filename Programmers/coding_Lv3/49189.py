from collections import deque

def solution(n, edge):
    table = [[] for _ in range(n + 1)]
    for ed in edge:
        table[ed[0]].append(ed[1])
        table[ed[1]].append(ed[0])
    start = 1
    q = deque([])
    q.append([start, 0])
    visited = [0] * (n + 1)
    visited[1] = 1
    visit_lst = [[start, 0]]
    answer = 0
    while q:
        x, cost = q.popleft()
        answer = max(answer, cost)
        for nex in table[x]:
            if visited[nex] == 0:
                q.append([nex, cost + 1])
                visited[nex] = 1
                visit_lst.append([nex, cost + 1])
    cnt = 0
    for a, b in visit_lst:
        if b == answer:
            cnt += 1

    return cnt