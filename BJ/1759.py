# bfs 하면 시간초과나옴
# from collections import deque
#
# L, C = map(int, input().split())
# lst = list(map(str, input().split()))
# lst.sort()
# candidates = []
# # a c i s t w
# for i in range(C):
#     q = deque()
#     q.append([lst[i]])
#     keyV = 0
#     while q:
#         tmp = q.popleft()
#         if len(tmp) == L:
#             keyV = 0
#             mo = 0
#             za = 0
#             for word in tmp:
#                 if word in ['a','e','i','o','u']:
#                     mo += 1
#                 else:
#                     za += 1
#             if mo>=1 and za>=2:
#                 tmp.sort()
#                 n_ans = ''.join(tmp)
#                 if n_ans not in candidates:
#                     candidates.append(n_ans)
#         else:
#             for keyV in range(i+1,C):
#                 if lst[keyV] not in tmp:
#                     q.append(tmp+[lst[keyV]])
#
# for c in candidates:
#     print(c)




# from itertools import combinations
#
# L, C = map(int, input().split())
# word_list = set(input().split())
#
# ## A(=모음), B(=자음)
# A = set(['a', 'e', 'i', 'o', 'u'])
# B = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
#
# ## word_list의 모음
# word_list_A = word_list & A
#
# for next in combinations(sorted(word_list), L):
#     num = len(set(next) & word_list_A)
#     if num == 0 or L - num < 2: continue
#     print(''.join(next))


# 재도전 필요
from copy import deepcopy

l, c = map(int, input().split())
alpha = list(map(str,input().split()))

alpha.sort()
m_lst = ['a','e','i','o','u']

visited = [0]*c


def dfs(now, cnt, candidate, z, m):
    if cnt == l:
        if z >= 2 and m >= 1:
            print(''.join([str(ch) for ch in candidate]))
    else:
        for i in range(now+1, c):
            if not visited[i]:
                visited[i] = 1
                candi = deepcopy(candidate)
                candi.append(alpha[i])
                if alpha[i] in m_lst:
                    dfs(i, cnt + 1, candi, z, m+1)
                else:
                    dfs(i, cnt + 1, candi, z+1, m)
                visited[i] = 0

dfs(-1,0,[],0,0)