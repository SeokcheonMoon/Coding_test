def solution(my_string):
    list_string = list(my_string)
    list_answer = []
    for x in range(len(list_string)):
        list_answer.append(list_string[x].lower())
    list_answer.sort()
    answer = "".join(list_answer)
    return answer