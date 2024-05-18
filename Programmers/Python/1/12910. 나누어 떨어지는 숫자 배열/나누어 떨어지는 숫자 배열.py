def solution(arr, divisor):
    answer = []
    for x in arr :
        if x % divisor == 0:
            answer.append(x)
    if len(answer) == 0:
        answer = [-1]
    answer.sort(reverse=False)
    return answer