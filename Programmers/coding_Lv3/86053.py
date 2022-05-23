# e다시풀기 필수

def solution(a, b, g, s, w, t):
    INF =int(1e10)
    answer = INF
    start, end = 0, INF
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0
        for i in range(len(g)):
            cur_g, cur_s, cur_w, cur_t = g[i], s[i], w[i], t[i]
            cnt = mid // (cur_t * 2)
            if mid % (cur_t * 2) >= cur_t:
                cnt += 1
            if cur_g < cnt * cur_w:
                gold += cur_g
            else:
                gold += cnt * cur_w

            if cur_s < cnt * cur_w:
                silver += cur_s
            else:
                silver += cnt * cur_w

            if cur_g + cur_s < cnt * cur_w:
                total += cur_g + cur_s
            else:
                total += cnt * cur_w
        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer