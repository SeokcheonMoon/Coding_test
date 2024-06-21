def solution(x, n):
    value = 0
    answer = []
    for i in range(n):
        value = value + x
        answer.append(value)
    return answer