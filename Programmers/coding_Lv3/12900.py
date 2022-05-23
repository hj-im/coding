def solution(n):
    a,b = 1,2
    for i in range(3,n+1):
        c = (a+b)
        if a>b: b = c
        else: a = c
    return c % 1000000007