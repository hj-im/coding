#주차요금계산
import math
import datetime

def time_caluculate(in_,out_):
    in_c,in_m = in_.split(':')
    out_c,out_m = out_.split(':')
    # datetime(2018, 7, 13, 21, 40, 5)
    tt_in = datetime.datetime(1,1,1,int(in_c),int(in_m),0)
    tt_out = datetime.datetime(1,1,1,int(out_c),int(out_m),0)
    time_ = (tt_out - tt_in).seconds/60
    # print('time',time_)
    # time_ = math.ceil(time_/10)
    return int(time_)

def record_time_check_func(lst,per_f,per_min,base_time):
    ans = 0
    # print('lst',lst)
    if len(lst) % 2 == 0:
        n = int(len(lst) / 2)
        for i in range(n):
            # print(lst[i*2:i*2+1])
            in_, out_ = lst[i*2],lst[i*2+1] # in_,out_ = '??:??'
            _time_ = time_caluculate(in_,out_)
            ans += _time_ 
    else:
        n = int(len(lst) // 2) + 1
        for i in range(n):
            if i == n-1:
                in_, out_ = lst[i*2], "23:59" # in_,out_ = '??:??'

                _time_ = time_caluculate(in_,out_)
                ans += _time_           
            else:
                in_, out_ = lst[i*2],lst[i*2+1] # in_,out_ = '??:??'
                _time_ = time_caluculate(in_,out_)
                ans += _time_ 
    # print('ans',ans)
    if ans<base_time:
      return 0
    return math.ceil((ans-base_time)/per_min) * per_f

def solution(fees, records):
    base_time, base_fee, per_min, per_fee = fees
    # 다른 방식의 array 고려해보기. 지금은 항상 1000개 만들어야하는 단점 존재
    record_dic = {}
    for _record_ in records:
        _t_, _number_, _inout_ = _record_.split(' ')
        
        if _number_ not in record_dic.keys():
            record_dic[_number_] = [_t_]
        else:
            record_dic[_number_].append(_t_)
    answer = []
    for key_ in record_dic.keys():
        final_fee = base_fee + record_time_check_func(record_dic[key_], per_fee,per_min,base_time)
        answer.append([int(key_),final_fee])

    # print(answer)
    answer.sort(key=lambda x:x[0])
    answer = [_[1] for _ in answer ]
    return answer
