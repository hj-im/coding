def solution(n, k, cmd):
    answer = ''
    llst = {0: [n - 1, 1]}
    for i in range(1, n):
        if i == n - 1:
            llst[i] = [i - 1, 0]
        else:
            llst[i] = [i - 1, i + 1]

    del_lst = []
    for name in cmd:
        if len(name) == 1:
            if name == 'C':
                llst[llst[k][0]][1] = llst[k][1]
                llst[llst[k][1]][0] = llst[k][0]
                del_lst.append([k, llst[k]])
                tmp = llst[k]
                del (llst[k])

                if tmp[1] == 0:
                    k = tmp[0]
                else:
                    k = tmp[1]
            else:
                current, cuurent_llst = del_lst.pop()
                prev_l, next_l = cuurent_llst
                llst[current] = [prev_l, next_l]
                llst[prev_l][1] = current
                llst[next_l][0] = current

        else:
            a, b = name.split(' ')
            count = 0
            if a == 'D':
                while count < int(b):
                    k = llst[k][1]
                    count += 1
            else:
                while count < int(b):
                    k = llst[k][0]
                    count += 1
    for i in range(n):
        if llst.get(i) is None:
            answer += 'X'
        else:
            answer += 'O'
    return answer