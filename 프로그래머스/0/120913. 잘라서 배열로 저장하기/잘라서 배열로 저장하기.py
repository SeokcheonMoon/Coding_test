def solution(my_str, n):
    k = 0
    answer = []
    while True:
        if k+n >= len(my_str):
            answer.append(my_str[k:len(my_str)])
            break
        else:    
            answer.append(my_str[k:k+n])
        k= k+n
    return answer