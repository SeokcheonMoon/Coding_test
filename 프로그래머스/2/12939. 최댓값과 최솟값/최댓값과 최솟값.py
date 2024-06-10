def solution(s):
    list_s = s.split()
    list_s = list(map(int,list_s))
    list_answer = []
    list_answer.append(min(list_s))
    list_answer.append(max(list_s))
    list_answer = list(map(str,list_answer))
    answer = " ".join(list_answer)
    return answer