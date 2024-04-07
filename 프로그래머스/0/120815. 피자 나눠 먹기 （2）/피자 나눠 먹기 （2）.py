def solution(n):
    for x in range(1,101):
        value = 6*x
        if value%n == 0:
            answer = x
            break
    return answer