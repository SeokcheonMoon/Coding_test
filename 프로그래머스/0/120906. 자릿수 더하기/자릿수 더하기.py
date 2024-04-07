def solution(n):
    str_num = str(n)
    answer = 0
    for x in range(len(str_num)) :
        answer = answer + int(str_num[x])
    return answer