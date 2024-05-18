def solution(phone_number):
    list_number = list(phone_number)

    list_answer = []
    for x in range(len(list_number)-4):
        list_answer.append("*")
    for y in range(len(list_number)-4,len(list_number)):
        list_answer.append(list_number[y])
    answer = "".join(list_answer)
    return answer