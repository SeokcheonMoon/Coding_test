def testcase():

    while True:
        str_first, str_second = input().split()
        num_first = int(str_first)
        num_second = int(str_second)
        
        if num_first == 0 or num_second == 0 :
            break
        else :
            print("{}".format(num_first+num_second))
    return 0

testcase()