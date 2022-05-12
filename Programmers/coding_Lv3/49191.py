
def solution(n, results):
    inf = int(1e9)
    table = [[inf] * (n + 1) for _ in range(n + 1)]
    for result in results:
        a, b = result
        table[b][a] = 1
    for i in range(1, n + 1):
        table[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])

    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if table[i][j] != inf or table[j][i] != inf:
                cnt += 1
        if cnt == n:
            ans += 1

    return ans