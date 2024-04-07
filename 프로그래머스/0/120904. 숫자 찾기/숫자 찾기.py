def solution(num, k):
    str_num =str(num)
    list_num = list(map(int,str_num))


    for x in range(len(list_num)):
        if list_num[x] == k :
            answer = x+1
            break
        else :
            answer = -1
    return answer