n = int(input())
m = int(input())
lst = []
for i in range(m):
  lst.append(list(map(int,input().split())))
inf_ = 1e9
table = [[inf_]*(n+1) for _ in range(n+1)]
for ls in lst:
  a,b,c = ls
  table[a][b]=min(c,table[a][b])
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      table[i][j] =0

for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      table[j][k] = min(table[j][k],table[j][i]+table[i][k])

for i in range(1,n+1):
  for j in range(1,n+1):
    if table[i][j] == inf_:
        print(0,end=' ')
    else:
        print(table[i][j],end=' ')
  print()    
