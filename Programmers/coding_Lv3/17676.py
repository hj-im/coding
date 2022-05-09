def lengthFunc(inp):
    if len(inp)>2:
        s,ms = inp[:-1].split('.')
        out_t = float(s)*1000 + float(ms)
    else:
        out_t = float(inp[:-1])*1000
    return out_t

def timesFunc(inp):
    h,m,s = inp.split(':')
    out_t = float(h)*3600 + float(m) * 60 + float(s)
    return out_t * 1000

def solution(lines):
    save = 0
    lst = []
    for line in lines:
        dates, times, length = line.split(' ')
        start = timesFunc(times) - lengthFunc(length)+1
        end = timesFunc(times)
        lst.append([start,end])
    for start,end in lst:
        cnt = [0]*2
        for t_s,t_e in lst:
            if start <=t_s <= start + 999  or start <= t_e <= start + 999 or (start>=t_s and t_e>=start+999):
                cnt[0]+=1
            if end <= t_s <= end + 999 or end <= t_e <= end + 999 or (end>=t_s and t_e>=end+999):
                cnt[1]+=1
        save = max(save, max(cnt))
    return save