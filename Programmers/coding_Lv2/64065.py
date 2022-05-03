def solution(s):
    ls = s[1:-1]
    ch = [0]
    for i in range(1, len(ls) - 1):
        if ls[i - 1] == '}' and ls[i] == ',' and ls[i + 1] == '{':
            ch.append(i)
    candidate = []
    ch.append(len(ls))
    for c in range(len(ch) - 1):
        if c == 0:
            candidate.append(ls[ch[c] + 1:ch[c + 1] - 1].split(','))
        else:
            candidate.append(ls[ch[c] + 2:ch[c + 1] - 1].split(','))

    candidate.sort(key=lambda x: len(x))
    tset = set([])
    answer = []
    for item in candidate:
        ans = set(item) - tset
        tset = tset | ans
        answer.append(int(ans.pop()))
    return answer