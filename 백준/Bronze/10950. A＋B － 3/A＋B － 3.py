def case():
    num_case = input()
    case = int(num_case)

    for x in range(case):
        str_A,str_B = input().split()
        A = int(str_A)
        B = int(str_B)
        print("{}".format(A+B))
    return 0

case()