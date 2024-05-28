def solution(seoul):
    for x in range(len(seoul)):
        if seoul[x] == "Kim":
            index = x
    answer = "김서방은 {}에 있다".format(index)
    return answer