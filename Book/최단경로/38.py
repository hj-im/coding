n,m =  map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
d = [[10000]*(n+1) for _ in range(n+1)]

for i in range(n+1):
  for j in range(n+1):
    if [i,j] in lst:
      d[i][j] = 1
    if i==j:
      d[i][j] =0
      # d[j][i] =3
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      d[a][b] = min(d[a][b],d[a][k]+d[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    d[a][b] = min(d[a][b],d[b][a])
    d[b][a] = min(d[a][b],d[b][a])
res = 0
for i in range(1,n+1):
  if sum(d[i][1:])<10000:
    res+=1

print(res)
