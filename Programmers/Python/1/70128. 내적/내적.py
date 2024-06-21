def solution(a, b):
    answer = 0
    for x in range(len(a)):
        value = a[x]*b[x]
        answer = answer + value
    return answer