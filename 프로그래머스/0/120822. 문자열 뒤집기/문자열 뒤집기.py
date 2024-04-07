def solution(my_string):
    list_string = list(my_string)
    list.reverse(list_string)
    answer = "".join(list_string)
    return answer