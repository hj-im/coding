N,M,K = map(int, input().split())
dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]
lst = []
# y x m s d
for _ in range(M):
    lst.append(list(map(int,input().split())))

table = [[[] for _ in range(N)]for _ in range(N)]
for move in range(K):

    while lst:
          y, x, m, s, d = lst.pop(0)

          ny = (y + dy[d] * s) % N
          nx = (x + dx[d] * s) % N
          table[ny][nx].append([m,s,d])


    for r in range(N):
        for c in range(N):
            if len(table[r][c]) >1:
                sum_m,sum_s,even,odd,cost = 0,0,0,0,len(table[r][c])
                while table[r][c]:
                    sub_m,sub_s,sub_d = table[r][c].pop(0)
                    sum_m += sub_m
                    sum_s += sub_s
                    if sub_d %2:
                        odd +=1
                    else:
                        even +=1
                sum_m = sum_m // 5
                sum_s = sum_s // cost
                if odd == cost or even == cost:
                    new_d = [0,2,4,6]
                else:
                    new_d = [1,3,5,7]
                if sum_m:
                    for direction in new_d:
                        lst.append([r,c,sum_m,sum_s,direction])
            elif len(table[r][c]) == 1:
                sub_m, sub_s, sub_d = table[r][c].pop(0)
                lst.append([r,c,sub_m,sub_s,sub_d])

print(sum([x[2] for x in lst]))

exit()
