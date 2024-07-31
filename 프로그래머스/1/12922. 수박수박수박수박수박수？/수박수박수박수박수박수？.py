def solution(n):
    a = n // 2
    b = n % 2

    list_answer = []
    for x in range(a):
        list_answer.append("수박")
    for y in range(b):
        list_answer.append("수")
    answer = "".join(list_answer)
    return answer