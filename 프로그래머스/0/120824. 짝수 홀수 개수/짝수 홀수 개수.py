def solution(num_list):
    a = 0
    b = 0
    for x in range(len(num_list)) :  
        if num_list[x] % 2 == 0 :
            a = a + 1
        elif num_list[x] % 2 == 1 :
            b = b + 1
    answer = []
    answer.append(a)
    answer.append(b)
    return answer