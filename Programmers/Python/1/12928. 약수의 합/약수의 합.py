def solution(n):
    list_count = []
    for x in range(1,n+1):
        if n%x == 0:
            list_count.append(x)
    answer = sum(list_count)
    return answer