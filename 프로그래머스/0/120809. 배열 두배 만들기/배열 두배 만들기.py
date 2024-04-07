def solution(numbers):
    answer = []
    for x in range(1,len(numbers)+1) : 
        value = numbers[x-1]*2
        answer.append(value)
    return answer