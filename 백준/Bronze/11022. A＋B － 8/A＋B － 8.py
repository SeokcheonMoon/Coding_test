def testcase():
    str_cycle = input()
    cycle = int(str_cycle)

    for x in range(cycle) :
            str_a,str_b = input().split()
            a = int(str_a)
            b = int(str_b)
            c= a+b
            print("Case #{}: {} + {} = {}".format(x+1,a,b,c))
testcase()