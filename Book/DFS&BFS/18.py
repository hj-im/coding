def seperate(s):
    cnt1 = 0
    cnt2 = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            return s[:i + 1], s[i + 1:]


def correct(s):
    x, y = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            x += 1
        elif x>=1:
            x -= 1
    if x == 0:
        return True
    return False




def inv(w):
    inv_ans = ''
    for w_ in range(len(w)):
        if w[w_] == '(':
            inv_ans +=')'
        else:
            inv_ans +='('
    return inv_ans
def solution(s):
    if s == '':
        return ''

    def dfs(s):
        if s == '':
            return s
        u, v = seperate(s)
        if correct(u):
            a = dfs(v)
            return u + a
        else:
            tmp = '('
            tmp += dfs(v)
            tmp += ')'
            tmp2 = u[1:-1]
            tmp2 = inv(tmp2)
            return tmp + tmp2

    answer = dfs(s)
    return answer
