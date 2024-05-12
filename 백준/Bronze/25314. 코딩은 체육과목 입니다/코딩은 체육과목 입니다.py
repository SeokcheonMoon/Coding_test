def four():
    str_number = input()
    number = int(str_number)

    num_repeat = number // 4

    list = []
    for x in range(num_repeat) :
        list.append("long")
        pass
        
    result = ' '.join(map(str, list))

    print("{} int".format(result))

four()