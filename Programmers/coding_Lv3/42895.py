def dpFunc(inp, n):
    a = inp + n
    b = inp - n
    c = inp * n
    d = inp
    if n != 0:
        d = inp // n
    return a, b, c, d


def solution(N, number):
    n_lst = [set() for _ in range(10)]
    n_lst[1].add(N)
    if number == N:
        return 1
    for i in range(2, 9):
        for k in range(1, i):
            for j in n_lst[i - k]:
                for l in n_lst[k]:
                    a, b, c, d = dpFunc(j, l)
                    n_lst[i].add(a)
                    n_lst[i].add(b)
                    n_lst[i].add(c)
                    n_lst[i].add(d)

        n_lst[i].add(int(str(N) * i))
        if number in n_lst[i]:
            return i
    return -1