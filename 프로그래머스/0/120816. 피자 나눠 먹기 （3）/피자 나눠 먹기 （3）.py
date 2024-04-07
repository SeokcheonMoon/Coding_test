def solution(slice, n):
    x = n % slice
    y = n // slice

    if x == 0 :
        answer = y
    else :
        answer = y + 1
    return answer