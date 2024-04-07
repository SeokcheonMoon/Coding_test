def solution(s):
    list_string = list(s)
    list_answer = []
    for x in range(len(list_string)):
        if list_string.count(list_string[x]) == 1:
            list_answer.append(list_string[x])
    list.sort(list_answer)
    answer = "".join(list_answer)
    return answer