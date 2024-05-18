def solution(s):
    list_s = list(s)

    if len(list_s)%2 == 1:
        answer = list_s[len(list_s)//2]
    else :
        answer = list_s[len(list_s)//2-1]+list_s[len(list_s)//2]
    return answer