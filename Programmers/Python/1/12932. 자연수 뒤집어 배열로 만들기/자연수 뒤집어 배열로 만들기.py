def solution(n):
    str_n = str(n)
    list_n = list(str_n)
    list_n.reverse()

    answer = []
    for x in range(len(list_n)):
        answer.append(int(list_n[x]))
    return answer