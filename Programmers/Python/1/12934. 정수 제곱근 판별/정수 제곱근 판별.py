def solution(n):
    if n % (n**0.5) == 0:
        answer = int(((n//(n**0.5))+1)**2)
    else :
        answer = -1
    return answer