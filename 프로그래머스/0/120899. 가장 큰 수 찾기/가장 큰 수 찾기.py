def solution(array):
    answer = []
    answer.append(max(array))

    for x in range(len(array)):
        if array[x] == max(array):
            answer.append(x)
    return answer