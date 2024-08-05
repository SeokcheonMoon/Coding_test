while True:
    str_first, str_second = input().split()
    first = int(str_first)
    second = int(str_second)

    if first == 0 and second == 0:
        break
    elif second % first == 0:
        print("factor")
    elif first % second == 0:
        print("multiple")
    else:
        print("neither")