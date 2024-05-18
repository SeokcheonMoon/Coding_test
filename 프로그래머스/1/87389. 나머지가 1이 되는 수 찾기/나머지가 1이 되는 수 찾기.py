def solution(n):
    list_number = []
    for x in range(1,n+1):
        if n%x == 1:
            list_number.append(x)
    answer = min(list_number)
    return answer