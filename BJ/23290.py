from collections import deque
M, S = map(int, input().split())
info = []
# 0 blank, 1 fish, 2 shark
board = [[[] for _ in range(4)] for _ in range(4)]
for i in range(M):
    fx, fy, direction = list(map(int,input().split()))
    info.append([fx-1,fy-1,direction,0])
    board[fx-1][fy-1].append(111)

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

shark_pos = list(map(int,input().split()))
shark_pos = [shark_pos[0]-1,shark_pos[1]-1,'',0]
board[shark_pos[0]][shark_pos[1]].append(112)
origin_board = [item[:] for item in board]


def dfunc(d):
    if d == 1:
        return 8
    else:
        return d-1

sdx = [0,-1,1,0,0]
sdy = [0,0,0,-1,1]
global_cnt = 0
while True:
    smells = []
    # 1 copy magic by shark
    copyed_fish = [item[:] for item in info]

    # 2 fishes move
    q = deque()
    q.append(info)
    while q:
        x, y, d, dcnt = q.popleft()

        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<4 and 0<=ny<4 and [nx,ny] not in smells and 112 not in board[nx][ny]:
            board[x][y].pop(0)
            board[nx][ny].append(111)
        elif dcnt<8:
            d = dfunc(d)
            q.append([x,y,d])

    # 3 shark moves 3 position

    sq = deque([shark_pos])
    s_possible = []
    while sq:
        sflag = 1
        s_x, s_y, sd, eated = sq.popleft()
        if len(sd) == 3:
            s_possible.append([shark_pos[0],shark_pos[1], sd, eated])
        for i in range(1,5):
            nx = s_x + sdy[i]
            ny = s_y + sdy[i]
            if 0<=nx<4 and 0<=ny<4:
                if len(sd)<3:
                    sq.append([nx,ny,sd+str(i),eated+len(board[nx][ny])])


    s_possible.sort(key=lambda x: (-x[3], int(x[2])))
    # s_final_direction = s_possible[0]
    s_f_x, s_f_y, s_f_d = s_possible[0]
    maxB = max(board)
    for i in list(s_f_d):
        n_f_x = s_f_x + s_x[int(i)]
        n_f_y = s_f_y + s_y[int(i)]
        if 112 not in board[s_f_x][s_f_y]:
            board[s_f_x][s_f_y] = []
            board[n_f_x][n_f_x].append(112)
            smells.append([n_f_x, n_f_x])
        s_f_x = n_f_x
        s_f_y = n_f_y

    # 4 smell of fish removed when made before 2 time
    board -= 1
    for i in range(4):
        for j in range(4):
            board[i][j] -=1
            if board[i][j] < 0:
                board[i][j] = 0

    # 5 copy magic complete
    for c_fish in copyed_fish:
        x,y,a,b = c_fish
        board[x][y] == 111

    if global_cnt == S:
        break
    global_cnt+=1



