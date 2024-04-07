def solution(my_string):
    list_answer = []
    list_string = list(my_string)
    pass
    for x in range(len(list_string)):
        if list_string[x].islower() == True :
            list_answer.append(list_string[x].upper())
        elif list_string[x].isupper() == True :
            list_answer.append(list_string[x].lower())
    answer = "".join(list_answer)
    return answer