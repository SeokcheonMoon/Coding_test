def min_max():
    str_count = input()
    str_list =input().split()
    num_list = list(map(int,str_list))

    print("{} {}".format(min(num_list),max(num_list)))
    return 0
min_max()