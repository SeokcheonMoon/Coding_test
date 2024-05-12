def solution(rsp):
    list_rsp = list(rsp)
    list_answer = []
    for x in range(len(list_rsp)):
        if list_rsp[x] == "0" :
            list_answer.append("5")
        elif list_rsp[x] == "2" :
            list_answer.append("0")
        elif list_rsp[x] == "5" :
            list_answer.append("2")

    answer = "".join(list_answer)
    return answer