from collections import deque
from itertools import combinations
n = int(input())
table = [list(map(str,input().split())) for _ in range(n)]

student = []
teacher = []
possible = []

for i in range(n):
    for j in range(n):
        if table[i][j] == 'T':
            teacher.append([i,j])
        elif table[i][j] == 'S':
            student.append([i,j])
        else:
            possible.append([i,j])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for install_b in combinations(possible,3):
    flag = 1
    problem = []
    for candi in install_b:
        if candi in possible:
            problem.append(candi)
    q = deque(teacher)
    while q:
        x,y = q.popleft()
        for i in range(4):
            for c in range(1,n):
                nx = x + c*dx[i]
                ny = y + c*dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if [nx,ny] in problem:
                        break
                    if [nx,ny] in student:
                        flag = 0
    if flag:
        break
if flag:
    print("YES")
else:
    print("NO")
