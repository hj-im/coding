from collections import deque

# if __name__ == '__main__':
def solution(N,M,origin_table):
    #
    # N, M = map(int,input().split())
    # origin_table = [list(map(str,input())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if origin_table[i][j] == 'R':
                red = (i, j)
            elif origin_table[i][j] == 'B':
                blue = (i, j)
            elif origin_table[i][j] == 'O':
                target = (i, j)
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque()
    q.append([red,blue])
    def move_func(i,x,y,table):
            # for i in range(4):
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]
                if table[nx][ny] == '#':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                elif table[nx][ny] == 'O':
                    break

            return nx,ny

    def bfs(red, blue, table):
        x, y = red
        a, b = blue
        q = deque()
        q.append((x,y,a,b))
        visited = []
        visited.append((x,y,a,b))
        cnt = 0
        while q:
            for _ in range(len(q)):
                x, y ,a, b = q.popleft()
                if cnt > 10:
                    # print(-1)
                    return -1
                if table[x][y] == 'O':
                    # print(cnt)
                    return cnt
                for i in range(4):
                    nx,ny = move_func(i,x,y,table)
                    na,nb = move_func(i,a,b,table)
                    if table[na][nb] == 'O':
                        continue
                    if nx == na and ny == nb:
                        if abs(nx - x) + abs(ny - y) > abs(na - a) + abs(nb - b):
                            nx -= dx[i]
                            ny -= dy[i]
                        else:
                            na -= dx[i]
                            nb -= dy[i]
                    if (nx, ny, na, nb) not in visited:
                        q.append((nx, ny, na, nb))
                        visited.append((nx, ny, na, nb))
            cnt += 1
        return -1

    ans = bfs(red,blue,origin_table)
    print(ans)

in2 = [['#','#','#','#','#'],['#','.','.','B','#'],['#','.','#','.','#'],['#','R','O','.','#'],['#','#','#','#','#']] # 1
in6 = [list(map(str,'#######')), list(map(str,'#R.O.B#')), list(map(str,'#######'))] # 5
in3 = [list(map(str,'#######')), list(map(str,'#...RB#')), list(map(str,'#.#####')),list(map(str,'#.....#')), list(map(str,'#####.#')), list(map(str,'#O....#')),list(map(str,'#######'))] #5
in4 = [list(map(str,'#######')), list(map(str,'#..R#B#')), list(map(str,'#.#####')),list(map(str,'#.....#')), list(map(str,'#####.#')), list(map(str,'#O....#')),list(map(str,'#######'))] #5

solution(5,5,in2)
solution(7,7,in3)
solution(7,7,in4)