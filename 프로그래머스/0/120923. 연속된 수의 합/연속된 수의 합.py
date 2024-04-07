def solution(num, total):
    value = 0
    for x in range(num):
        value = value + x
    first = int((total-value)/num)

    answer = []
    for y in range(first, first+num):
        answer.append(y)
    return answer