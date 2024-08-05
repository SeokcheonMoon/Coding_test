def solution(left, right):
    list_value = []
    list_result = []
    for x in range(left, right+1):
        for y in range(1,x+1):
            if x % y == 0:
                list_value.append(y)
        set_value = set(list_value)
        list_result.append(set_value)
        list_value = []

    answer = 0
    for x in range(len(list_result)):
        if len(list_result[x]) % 2 == 0 :
            answer = answer + max(list_result[x])
        else :
            answer = answer - max(list_result[x])
    return answer