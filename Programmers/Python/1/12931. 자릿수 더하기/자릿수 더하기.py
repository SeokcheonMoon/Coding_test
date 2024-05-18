def solution(n):
    str_number = str(n)
    list_number = list(str_number)

    answer=0
    for x in range(len(list_number)):
        answer = answer+int(list_number[x])

    return answer