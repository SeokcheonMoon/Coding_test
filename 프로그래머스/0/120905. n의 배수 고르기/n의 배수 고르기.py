def solution(n, numlist):
    answer = []
    for x in range(len(numlist)) :
        if numlist[x] % n == 0:
            answer.append(numlist[x])
    return answer