def solution(chicken):
    str_chicken = str(chicken)

    list_answer = []
    list_plus = []
    value = chicken // 10
    plus = chicken % 10

    for x in range(len(str_chicken)):
        list_answer.append(value)
        list_plus.append(plus)
        plus = value % 10
        value = value // 10

    answer = sum(list_answer) + sum(list_plus)//10
    if sum(list_plus) // 10 + sum(list_plus) % 10 >= 10:
        answer = answer + 1
    return answer