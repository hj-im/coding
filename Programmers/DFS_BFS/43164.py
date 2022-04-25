from collections import deque
def solution(tickets):
    tickets.sort(key = lambda x:x[1])
    #print(tickets)
    start = [i for i in range(len(tickets)) if tickets[i][0] == "ICN"]
    #print(start)
    answer = []
    for s in start:
        q = deque([])
        q.append([s])
        if not answer:
            while q:
                #path 는 숫자로 구성
                path = q.popleft()
                if len(path) == len(tickets):
                    answer = [tickets[x][0] for x in path] + [tickets[path[-1]][1]]
                    break
                for i in range(len(tickets)):
                    if i not in path and tickets[path[-1]][1] == tickets[i][0]:
                        # print(i)
                        q.append(path+[i])
            # answer = []
    return answer