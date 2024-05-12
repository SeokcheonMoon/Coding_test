def solution(my_string, num1, num2):
    list_string  = list(my_string)

    a = list_string[num1]
    b = list_string[num2]

    list_string[num2] = a
    list_string[num1] = b

    answer = "".join(list_string)
    return answer