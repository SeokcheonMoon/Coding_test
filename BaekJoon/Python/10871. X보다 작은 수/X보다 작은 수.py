def testcase():

    str_count, str_border = input().split()
    num_count = int(str_count)
    num_border = int(str_border)

    str_list_number = input().split()
    list_number = list(map(int,str_list_number))

    for x in range(len(list_number)):

        if list_number[x] < num_border :
            print(list_number[x], end=" ")

    return 0

testcase()