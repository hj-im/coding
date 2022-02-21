import math 
def conver_func(n,k):
    conv_ = ''
    while n>0:
        n,mod_ = divmod(n,k)
        conv_ +=str(mod_)
    
    return conv_[::-1]

def is_prime_number_func(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    
    return True

def solution(n, k):
    answer = 0
    conver_n = conver_func(n, k)
    # print(conver_n)
    lst = list(conver_n)
    
    array = []
    # print(lst)
    t = 0
    # start = 0
    # end = 3
    for i in range(len(lst)):
        # end = 3
        if int(lst[i]) == 0 and t != i:
            array.append([t,i])
            t = i+1
            # end = 1
        elif int(lst[i]) == 0 and t==i :
            t = i+1
            # end = 0
        elif i == len(lst)-1 and int(lst[i]) != 0 :
            array.append([t,i+1])
        # print(end)
    candidate = []
    tt = 0
    # print(array)
    for a,b in array:
        candidate.append(conver_n[a:b])
    # print(candidate)
    for candi in candidate:
        candi_int = int(candi)
        if candi_int != 1 and is_prime_number_func(candi_int):
            answer += 1
    return answer
