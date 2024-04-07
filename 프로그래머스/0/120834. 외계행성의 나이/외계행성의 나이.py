def solution(age):
    string = "abcdefghijklmnopqrstuvwxyz"
    list_string = list(string)

    str_age = str(age)
    list_age = list(map(int,str_age))

    list_answer = []
    for x in range(len(list_age)):
        value = list_string[list_age[x]]
        list_answer.append(value)

    answer = "".join(list_answer)
    return answer