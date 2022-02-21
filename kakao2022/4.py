# 양궁대회
from collections import deque

def bfs(n, info):
    answer = []
    q = deque([(0,[0]*11)])
    maxVal = 0
    while q:
        target, cnt = q.popleft()
        # print(target,cnt)
        if sum(cnt) >n:
            continue
        elif target ==10:
            last_ = cnt.copy()
            last_[target] = n-sum(last_)
            q.append((12,last_))
            
        elif sum(cnt) < n:
            shot_ = cnt.copy()
            shot_[target] = info[target]+1
            q.append((target+1,shot_))
            
            dont_shot_ = cnt.copy()
            dont_shot_[target] = 0
            q.append((target+1,dont_shot_))
            
        elif sum(cnt) == n:
            a,b = 0,0 # 어피치, 라이언 
            for i in range(11):
                if not (info[i] == 0 and cnt[i]==0):
                    if info[i]>=cnt[i]:
                        a += 10-i
                    else:
                        b += 10-i
            if a < b :
                score = b-a
                if maxVal>score:
                    continue
                elif maxVal<score:
                    maxVal = score
                    answer=[]
                    answer.append(cnt)  
                else:
                    answer.append(cnt)  
    return answer


def solution(n, info):
    final_ = bfs(n,info)
    if not final_:
        return [-1]
    elif len(final_) == 1:
        return final_[0]
    else:
        return final_[-1]
