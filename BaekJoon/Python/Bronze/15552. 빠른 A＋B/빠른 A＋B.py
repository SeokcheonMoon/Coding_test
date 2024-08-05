import sys

def testcase() :
    str_cycle = sys.stdin.readline()
    cycle = int(str_cycle)
    for x in range(cycle) :
        str_a,str_b = sys.stdin.readline().split()
        a = int(str_a)
        b = int(str_b)
        print(a+b)

testcase()