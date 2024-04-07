def solution(numbers, num1, num2):
    answer = []
    for x in range(num1, num2+1) :
        answer.append(numbers[x])
    return answer