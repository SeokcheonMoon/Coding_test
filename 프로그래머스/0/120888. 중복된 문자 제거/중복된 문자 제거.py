def solution(my_string):
    list_string = list(my_string)
    list_answer = []

    for x in range(len(list_string)) :
        if list_answer.count(list_string[x]) == 0 :
            list_answer.append(list_string[x])
    answer = "".join(list_answer)
    return answer