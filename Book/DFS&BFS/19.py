import copy
n = int(input())
a_lst = list(map(int,input().split()))
oper = list(map(int,input().split()))

ans = a_lst[0]
maxVal = -int(1e9)
minVal = int(1e9)
def dfs(ans, a_lst, oper_origin, t = 0):
    global minVal
    global maxVal
    if t == n:
        minVal = min(minVal, ans)
        maxVal = max(maxVal, ans)
        return
    else:
      for i in range(4):
         if oper_origin[i]!=0:
          if i == 0:
              oper_lst0 = copy.deepcopy(oper_origin)
              # print(t)
              ans0 = ans + a_lst[t]
              oper_lst0[i] -= 1
              dfs(ans0, a_lst, oper_lst0,t+1)
              # oper_lst[i] += 1
          elif i == 1:
              oper_lst1 = copy.deepcopy(oper_origin)
              ans1 = ans - a_lst[t]
              oper_lst1[i] -= 1
              dfs(ans1, a_lst, oper_lst1,t+1)
              # oper_lst[i] += 1
          elif i == 2:
              oper_lst2 = copy.deepcopy(oper_origin)
              ans2 = ans * a_lst[t]
              oper_lst2[i] -= 1
              dfs(ans2,a_lst, oper_lst2,t+1)
              # oper_lst[i] += 1
          elif i == 3:
              oper_lst3 = copy.deepcopy(oper_origin)
              if ans <0:
                  ans3 = (abs(ans) // a_lst[t]) * (-1)
              else:
                  ans3 = abs(ans) // a_lst[t]
              oper_lst3[i] -= 1
              dfs(ans3, a_lst,oper_lst3,t+1)
              # oper_lst[i] += 1

dfs(ans, a_lst, oper, 1)
print(maxVal)
print(minVal)
