def solution(n):
    list_number = []
    for number in range(1,n+1) :
        if number % 2 == 0 :
            list_number.append(number)
    answer = 0
    for index in range(0,len(list_number)+1):
        if index == len(list_number) : 
            break
        else:
            answer = answer + list_number[index]
    return answer