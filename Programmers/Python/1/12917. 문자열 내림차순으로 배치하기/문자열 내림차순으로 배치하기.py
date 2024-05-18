def solution(s):
    list_s = list(s)
    list_s.sort(reverse = True)
    answer = "".join(list_s)
    return answer