def solution(n, t, m, timetable):
    answer = '09:00'

    def split_time(x):
        a, b = x.split(':')
        return int(a) * 60 + int(b)

    def change_time(x):
        a, b = x // 60, x % 60
        return f'{str(a).zfill(2)}:{str(b).zfill(2)}'

    times = [split_time(x) for x in timetable]
    times.sort()
    a = 0
    bustime = [9 * 60 + t * i for i in range(n)]

    for bt in bustime:
        cnt = 0
        while cnt < m and a < len(times) and times[a] <= bt:
            a += 1
            cnt += 1
        if cnt < m:
            answer = change_time(bt)
        else:
            answer = change_time(times[a - 1] - 1)
    return answer
