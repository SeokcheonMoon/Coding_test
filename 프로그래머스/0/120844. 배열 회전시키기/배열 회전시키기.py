def solution(numbers, direction):
    answer = []
    if direction == "left":
        for x in range(1,len(numbers)):
            answer.append(numbers[x])
        answer.append(numbers[0])

    else :
        answer.append(numbers[len(numbers)-1])
        for y in range(0,len(numbers)-1):
            answer.append(numbers[y])
    return answer