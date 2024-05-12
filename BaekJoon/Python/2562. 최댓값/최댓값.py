def max_min():
    list_number = []
    for x in range(9):
        str_number = input()
        list_number.append(str_number)
        result_list = list(map(int,list_number))
        answer = max(result_list)
        if result_list[x] == answer :
            index_answer = result_list.index(answer)
    print(answer)
    print(index_answer+1)

max_min()