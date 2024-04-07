def solution(cipher, code):
    list_cipher = list(cipher)
    list_answer = []
    for x in range(1,len(cipher)+1):
        if x % code == 0 :
            list_answer.append(list_cipher[x-1])
    answer = "".join(list_answer)
    return answer