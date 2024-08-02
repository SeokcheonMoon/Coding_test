def solution(arr1, arr2):
    list_answer = []
    for x in range(len(arr1)):
        list_value = []
        for y in range(len(arr1[x])):
            list_value.append(arr1[x][y]+arr2[x][y])
        list_answer.append(list_value)
    return list_answer