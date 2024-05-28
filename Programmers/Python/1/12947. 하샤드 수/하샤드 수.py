def solution(x):
    list_number = list(str(x))

    value = sum(list(map(int,list_number)))

    if x%value == 0 :
        answer = True
    else : 
        answer = False
    return answer