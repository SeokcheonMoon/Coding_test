def solution(my_string):
    list_string = list(my_string)
    answer = 0
    for x in range(len(list_string)) :
        if list_string[x].isdecimal() == True:
            answer = answer + int(list_string[x])
    return answer