def solution(absolutes, signs):
    list_answer = []
    for x in range(len(absolutes)):
        if signs[x] == True:
            list_answer.append(0 + absolutes[x])
        elif signs[x] == False: 
            list_answer.append(0 - absolutes[x])
    answer = sum(list_answer)
    return answer