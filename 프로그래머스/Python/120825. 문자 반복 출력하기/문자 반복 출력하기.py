def solution(my_string, n):
    list_answer = []
    for x in range(len(my_string)):
        for y in range(n):
            list_answer.append(my_string[x])
    answer = "".join(list_answer)
    return answer