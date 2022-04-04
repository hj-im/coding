n = list(str(input()))
n_ = len(n)
left = sum([int(i) for i in n[:n_//2]])
right = sum([int(i) for i in n[n_//2:]])
if left == right:
  print('LUCKY')
else:
  print('READY')
