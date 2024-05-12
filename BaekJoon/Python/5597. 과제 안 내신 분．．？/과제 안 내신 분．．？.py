origin_list = []
for x in range(30) :
    origin_list.append(x+1)

list_number = []
for x in range(28) :
    str_number = input()
    number = int(str_number)
    list_number.append(number)

result=[]
for y in origin_list :
    if y not in list_number:
        result.append(y)

result = sorted(result)
print(result[0])
print(result[1])