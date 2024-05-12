def sum():
    str_num = input()
    number = int(str_num)
    sum = 0
    for x in range(1,number+1) :
        sum = sum + x
    print("{}".format(sum))

    return 0

sum()