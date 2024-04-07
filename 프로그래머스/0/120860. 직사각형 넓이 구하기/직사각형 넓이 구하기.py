def solution(dots):
    list_answer = []
    a = int(((dots[0][0]-dots[1][0])**2+(dots[0][1]-dots[1][1])**2)**0.5)
    b = int(((dots[0][0]-dots[2][0])**2+(dots[0][1]-dots[2][1])**2)**0.5)
    c = int(((dots[0][0]-dots[3][0])**2+(dots[0][1]-dots[3][1])**2)**0.5)
    list_answer.append(a)
    list_answer.append(b)
    list_answer.append(c)
    list_answer.remove(max(list_answer))
    answer = list_answer[0]*list_answer[1]
    return answer