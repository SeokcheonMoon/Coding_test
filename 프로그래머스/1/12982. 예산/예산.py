def solution(d, budget):
    d.sort(reverse=False)

    list_answer = []
    for x in range(len(d)):
        budget = budget - d[x]
        if budget >= 0:
            list_answer.append(d[x])
        else:
            break
    answer = len(list_answer)
    return answer