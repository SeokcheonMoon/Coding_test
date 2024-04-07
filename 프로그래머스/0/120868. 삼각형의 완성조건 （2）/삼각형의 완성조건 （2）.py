def solution(sides):
    sum = 0
    for x in range(len(sides)):
        sum = sum + sides[x]
    list_answer = []
    for y in range(max(sides)-min(sides)+1, sum):
        list_answer.append(y)

    answer = len(list_answer)
    return answer