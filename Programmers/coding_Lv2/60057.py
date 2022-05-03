def solution(s):
    ans = len(s)
    for s_range in range(1, len(s) // 2 + 1):
        char = ''
        start = s[0:s_range]
        cnt = 1
        for index in range(s_range, len(s), s_range):

            if s[index:index + s_range] == start:
                cnt += 1
            else:
                char += str(cnt) + start if cnt >= 2 else start
                start = s[index:index + s_range]
                cnt = 1
        char += str(cnt) + start if cnt >= 2 else start
        ans = min(ans, len(char))

    return ans