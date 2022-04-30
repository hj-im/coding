def dice_update(i, dice):

    n_dice = [0] * 7
    if i == 1:
        d_change = [4, 2, 1, 6, 5, 3]
    elif i == 2:
        d_change = [3, 2, 6, 1, 5, 4]
    elif i == 3:
        d_change = [5, 1, 3, 4, 6, 2]
    elif i == 4:
        d_change = [2, 6, 3, 4, 1, 5]

    for j in range(1, 7):
        n_dice[j] = dice[d_change[j-1]]

    return n_dice


def simul(pos, table):
    dice = [0] * 7
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    for i in direction:
        x, y = pos
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            pos = (nx,ny)
            dice = dice_update(i, dice)
            #
            print(dice[1])
            #
            if table[nx][ny] == 0:
                table[nx][ny] = dice[6]
            else:
                dice[6] = table[nx][ny]
                table[nx][ny] = 0


if __name__ == '__main__':
    N, M, X, Y, K = map(int, input().split())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    direction = list(map(int, input().split()))

    start = (X, Y)

    simul(start, lst)
    # exit()