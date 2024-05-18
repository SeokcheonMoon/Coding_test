def solution(num):
    for x in range(1,501) :
        if num == 1:
            answer = x-1
            break
        if num % 2 == 0 : 
            num = num/2
        else :
            num = 3*num+1
    if num != 1:
        answer = -1
    return answer