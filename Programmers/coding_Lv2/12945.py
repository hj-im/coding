# 1번 방법
def solution(n):
    a, b = 0, 1
    for _ in range(1,n):
        a, b = b, a+b
    return b%1234567

# 1번 방법이 더 빠름
# 2번 방법
def solution(n):
    pivo = [0,1]
    for i in range(1,n):
        pivo.append(pivo[i-1] + pivo[i])
    return pivo[-1]%1234567