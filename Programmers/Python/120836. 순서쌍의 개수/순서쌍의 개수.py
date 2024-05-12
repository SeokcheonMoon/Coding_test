def solution(n):
    list_answer = []
    for x in range(1,n+1):
        if n%x == 0:
            list_answer.append(x)
    answer = len(list_answer)
    return answer