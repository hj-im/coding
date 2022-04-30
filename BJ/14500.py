# 재도전
def dfs(k, temp, x, y):
    global answer
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    if k == 4:
        answer = max(answer, temp)
        return
    if temp + (4 - k) * max_val < answer:
        return
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if k == 2:
                    dfs(k + 1, temp + table[nx][ny], x, y)
                dfs(k + 1, temp + table[nx][ny], nx, ny)
                visited[nx][ny] = False
    return


if __name__ == '__main__':

    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    max_val = max(map(max, table))

    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(1, table[i][j], i, j)
            visited[i][j] = False
    print(answer)