def solution(strlist):
    answer = []
    for x in range(0,len(strlist)) : 
        answer.append(len(list(strlist[x])))
    return answer