# 재도전
from itertools import permutations


def find_ban(candidate, banned_id):
    for i in range(len(candidate)):
        if len(candidate[i]) != len(banned_id[i]):
            return False
        for j in range(len(candidate[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != candidate[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    n = len(banned_id)
    for candidate in permutations(user_id, n):
        if find_ban(candidate, banned_id):
            tmp = set(candidate)
            if tmp not in answer:
                answer.append(tmp)
    return len(answer)