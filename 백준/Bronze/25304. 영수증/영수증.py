def price() :
    str_price = input()
    price = int(str_price)
    str_count = input()
    count = int(str_count)

    sum = 0
    for x in range(count) :
        str_a,str_b = input().split()
        a = int(str_a)
        b = int(str_b)
        add = a*b
        sum = sum + add

    if price == sum :
        print("{}".format("Yes"))
    else :
        print("{}".format("No"))

    return

price()