def solution(str1, str2):
    if str1.count(str2) > 0 :
        answer = 1
    elif str1.count(str2) == 0 :
        answer = 2
    return answer