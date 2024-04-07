def solution(n):
    a = n ** 0.5
    if n % a == 0:
        answer = 1
    elif n % a != 0:
        answer = 2
    return answer