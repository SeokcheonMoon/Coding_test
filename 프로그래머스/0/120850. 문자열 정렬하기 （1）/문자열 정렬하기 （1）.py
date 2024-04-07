def solution(my_string):
    answer = []
    for x in range(len(my_string)) : 
        if my_string[x].isdecimal() == True :
            answer.append(int(my_string[x]))
    answer.sort(reverse=False)
    return answer