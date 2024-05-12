def joining():

    str_cycle = input()
    cycle = int(str_cycle)

    list = []
    for x in range(cycle) :
        list.append("*")
        answer ="".join(list)
        print(answer.rjust(cycle))
joining()