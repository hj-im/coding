from collections import deque


def check(begin, target, l):
    c = 0
    for i in range(l):
        if begin[i] != target[i]:
            c += 1
    if c == 1:
        return 1
    else:
        return 0


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = []
    q = deque()
    q.append([begin, 0])
    while q:
        sub_begin, cost = q.popleft()
        for sub_target in words:
            if sub_target not in visited and check(sub_begin, sub_target, len(target)):
                if sub_target == target:
                    answer = cost + 1
                    break
                else:
                    q.append([sub_target, cost + 1])
                    visited.append(sub_target)

    return answer