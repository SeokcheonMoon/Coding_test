def solution(array, n):
    list_answer = []
    for x in range(len(array)):
        list_answer.append((n-array[x])**2)

    list_array = []
    for y in range(len(list_answer)):
        if list_answer[y] == min(list_answer):
            list_array.append(array[y])

    answer = min(list_array)
    return answer