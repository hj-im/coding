# from collections import defaultdict, deque
#
# def solution(enroll, referral, seller, amount):
#     table = {}
#     for lst in zip(enroll, referral):
#         table[lst[0]] = lst[1]
#     cost = {}
#     for lst in zip(seller, amount):
#         cost[lst[0]] = lst[1]
#
#     all_Cost = defaultdict(list)
#     for i, e in enumerate(enroll):
#         all_Cost[e].append(i)
#
#     n = len(seller)
#     for i in range(n):
#         sell_init = seller[i]
#         ct = 0
#         q = deque([])
#         q.append(sell_init)
#         while q:
#             sell = q.popleft()
#             if sell == sell_init:
#                 gain = cost[sell] * 100
#             else:
#                 gain = gain_div
#             gain_div = int(gain * 0.1)
#
#             n_gain = gain - gain_div
#             all_Cost[sell].append(n_gain)
#             if gain_div == 0:
#                 break
#             n_sell = table[sell]
#             if n_sell == '-':
#                 break
#             else:
#                 q.append(n_sell)
#     all_lst = sorted(all_Cost.values())
#     answer = []
#     for al in all_lst:
#         if len(al)>1:
#             answer.append(sum(al[1:]))
#         else:
#             answer.append(0)
#     return answer
from collections import defaultdict
import math


def solution(enroll, referral, seller, amount):
    table = {}
    for lst in zip(enroll, referral):
        table[lst[0]] = lst[1]
    # cost = {}
    # for lst in zip(seller, amount):
    #     cost[lst[0]] = lst[1]

    all_Cost = defaultdict(int)
    for e in enroll:
        all_Cost[e]=0

    n = len(seller)
    for i in range(n):
        sell_init = seller[i]
        market = amount[i] *100
        while 1:
            if market < 10:
                all_Cost[sell_init] += market
                break
            else:
                all_Cost[sell_init] += math.ceil(market * 0.9)
                if table[sell_init] == '-':
                    break
                market = math.floor(market * 0.1)
                sell_init = table[sell_init]
    all_lst = all_Cost.values()
    answer = list(all_lst)

    return answer

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])