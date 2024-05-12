def solution(my_string, letter):
    list_my_string = list(my_string)

    list_answer = []
    for x in range(0,len(list_my_string)) : 

        if list_my_string[x] != letter:
            list_answer.append(list_my_string[x])
    answer = "".join(list_answer)
    return answer