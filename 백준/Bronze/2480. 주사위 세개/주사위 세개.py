str_first,str_second,str_third = input().split()
num_first = int(str_first)
num_second = int(str_second)
num_third = int(str_third)

list_number = [num_first,num_second,num_third]
max_number = max(list_number)

if num_first == num_second == num_third :
    print("{}".format(10000 + num_first*1000))

elif num_first == num_second != num_third :
    print("{}".format(1000 + num_first*100))

elif num_second == num_third != num_first :
    print("{}".format(1000 + num_second*100))

elif num_first == num_third != num_second :
    print("{}".format(1000 + num_first*100))

else :
    print("{}".format(max(list_number)*100))