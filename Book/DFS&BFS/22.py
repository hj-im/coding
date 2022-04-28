from collections import deque
def move_possible(robot, board):
    candidate = []
    pos1, pos2 = robot
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        n_pos1 = (pos1[0]+dx[i], pos1[1]+dy[i])
        n_pos2 = (pos2[0]+dx[i], pos2[1]+dy[i])

        if board[n_pos1[0]][n_pos1[1]] == 0 and board[n_pos2[0]][n_pos2[1]] == 0:
            candidate.append((n_pos1, n_pos2))

    if pos1[0] == pos2[0]:
        if board[pos1[0] + 1][pos1[1]] == 0 and board[pos2[0] + 1][pos2[1]] == 0:
                candidate.append((pos2, (pos2[0] + 1, pos2[1])))
                candidate.append((pos1, (pos1[0] + 1, pos1[1])))
        if board[pos1[0] - 1][pos1[1]] == 0 and board[pos2[0] - 1][pos2[1]] == 0:
                candidate.append((pos2, (pos2[0] - 1, pos2[1])))
                candidate.append((pos1, (pos1[0] - 1, pos1[1])))

    else:
        if board[pos1[0]][pos1[1] + 1] == 0 and board[pos2[0]][pos2[1] + 1] == 0:
                candidate.append((pos2, (pos2[0],  pos2[1] + 1)))
                candidate.append((pos1, (pos1[0],  pos1[1] + 1)))
        if board[pos1[0]][pos1[1] - 1] == 0 and board[pos2[0]][pos2[1] - 1] == 0:
                candidate.append((pos2, (pos2[0], pos2[1] - 1)))
                candidate.append((pos1, (pos1[0], pos1[1] - 1)))
    return candidate


def solution(board):
    N = len(board)
    table = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            table[i + 1][j + 1] = board[i][j]
    current = ((1, 1), (1, 2))
    q = deque([])
    visited = set([current])
    q.append((current, 0))
    while q:
        pos_1, cost = q.popleft()
        if pos_1[0] == (N, N) or pos_1[1] == (N, N):
            break
        candidates = move_possible(pos_1, table)
        for candi in candidates:
            if candi not in visited:
                q.append((candi, cost + 1))
                visited.add(candi)
    return cost

#
# from collections import deque, defaultdict
#
#
# def pos_check(pos_a, table):
#     out = []
#     direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#     for y, x in direction:
#         n_1 = (pos_a[0][0] + y, pos_a[0][1] + x)
#         n_2 = (pos_a[1][0] + y, pos_a[1][1] + x)
#         if table[n_1[0]][n_1[1]] == 0 and table[n_2[0]][n_2[1]] == 0:
#             out.append((n_1, n_2))
#
#     # turn right
#     if pos_a[0][0] == pos_a[1][0]:
#         for i in [-1, 1]:
#             if table[pos_a[0][0] + i][pos_a[0][1]] == 0 and table[pos_a[1][0] + i][pos_a[1][1]] == 0:
#                 out.append((pos_a[0], (pos_a[0][0] + i, pos_a[0][1])))
#                 out.append((pos_a[1], (pos_a[1][0] + i, pos_a[1][1])))
#
#     # turn left
#     else:
#         for i in [-1, 1]:
#             if table[pos_a[0][0]][pos_a[0][1] + i] == 0 and table[pos_a[1][0]][pos_a[1][1] + i] == 0:
#                 out.append(((pos_a[0][0], pos_a[0][1] + i), pos_a[0]))
#                 out.append(((pos_a[1][0], pos_a[1][1] + i), pos_a[1]))
#     return out
#
#
# def solution(board):
#     N = len(board)
#     table = [[1] * (N + 2) for _ in range(N + 2)]
#     for i in range(N):
#         for j in range(N):
#             table[i + 1][j + 1] = board[i][j]
#     current = ((1, 1), (1, 2))
#     q = deque([])
#     visited = set([current])
#     q.append((current, 0))
#     while q:
#         pos_1, cnt = q.popleft()
#         if pos_1[0] == (N, N) or pos_1[1] == (N, N):
#             break
#         candidates = pos_check(pos_1, table)
#         for candi in candidates:
#             if candi not in visited:
#                 q.append((candi, cnt + 1))
#                 visited.add(candi)
#
#     answer = cnt
#     return answer