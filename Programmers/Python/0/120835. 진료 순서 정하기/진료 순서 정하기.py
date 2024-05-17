def solution(emergency):
    solving_list = []
    for x in range(len(emergency)):
        solving_list.append(emergency[x])

    solving_list.sort(reverse=True)
    answer = []
    for x in range(len(emergency)):
        answer.append(solving_list.index(emergency[x])+1)
    return answer