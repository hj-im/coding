import heapq

def solution(jobs):
    start = -1
    now = 0
    ans = 0
    lst = []
    n = len(jobs)
    m = len(jobs)
    while n:
        for a,b in jobs:
            if start< a <=now:

                heapq.heappush(lst, [b,a])
        if len(lst) > 0 :
            cur_l, cur_s = heapq.heappop(lst)
            start = now
            now += cur_l
            ans += (now-cur_s)
            n -= 1
        else:
            now +=1
    return int(ans/m)