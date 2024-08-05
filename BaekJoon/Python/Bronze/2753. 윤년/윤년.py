str_year = input()
num_year = int(str_year)

if num_year % 4 == 0 and num_year % 100 != 0 :
    print("{}".format(1))
elif num_year % 400 == 0 :
    print("{}".format(1))
else :
    print("{}".format(0))