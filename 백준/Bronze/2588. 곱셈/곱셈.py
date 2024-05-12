str_first = input()
str_second = input()

num_first = int(str_first)
num_second = int(str_second)

print("{}".format(num_first*(num_second%10)))
print("{}".format(num_first*(num_second//10%10)))
print("{}".format(num_first*(num_second//100)))
print("{}".format(num_first*num_second))