import copy
def solution(id_list, report, k):
	answer = [0] * len(id_list)
	report_list = {_ : set() for _ in id_list}
	count_list = {_ : 0 for _ in id_list}
	for i in report:
		a,b = i.split(' ')
		report_list[a].add(b)
	ban_list = []
	for j in report_list.keys():
		temp = list(report_list[j])
		for r in temp:
			count_list[r] += 1
			if count_list[r] == k:
				ban_list.append(r)
                
	for l1,l2 in enumerate(report_list.keys()):
		tt = list(report_list[l2])
		for tt_ in tt:
			if tt_ in ban_list:
				answer[l1] +=1
	return answer
