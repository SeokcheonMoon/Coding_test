def solution(array, commands):
    list_number = []
    for x in range(len(commands)) :
        list_number.append(sorted(array[commands[x][0] - 1:commands[x][1]])[commands[x][2] - 1])

    answer = list_number
    return answer