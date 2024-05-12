def solution(numbers):
    sum = 0
    for x in range(len(numbers)):
        sum = sum + numbers[x-1]
    answer = sum / len(numbers)
    return answer