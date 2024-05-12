def solution(box, n):
    list_answer = []
    for x in range(len(box)):
        list_answer.append(box[x]//n)

    answer = list_answer[0]*list_answer[1]*list_answer[2]
    return answer