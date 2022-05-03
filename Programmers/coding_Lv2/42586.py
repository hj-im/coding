def solution(progresses, speeds):
    end = []
    for x,y in zip(progresses,speeds):
        cal = int((100-x)/y)
        if (100-x)%y != 0 :
            cal +=1
        end.append(cal)
    answer = []
    cnt = 0
    dayVal = 0
    visited = [0]*len(end)
    for i in range(len(end)):
        for j in range(i,len(end)):
            if end[j]<=end[i] and visited[j] ==0:
                cnt+=1
                dayVal +=1
                visited[j] = 1
            else:
                break
        if dayVal != 0:
            answer.append(dayVal)
            dayVal = 0
        if cnt == len(end):
            break
    return answer

# 다른풀이
def solution(progresses, speeds):
    answer = []
    cnt = 0
    dayVal = 0
    while progresses:
        if progresses[0] + speeds[0] * dayVal >=100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
        else:
            if cnt>=1:
                answer.append(cnt)
                cnt = 0
            dayVal +=1
    answer.append(cnt)
    return answer