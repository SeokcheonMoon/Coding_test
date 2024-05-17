n = 12
answer = 28

약수 = 1,2,3,4,6,12
str_number = input()
int_number = int(str_number)
list_count = []
for x in range(1,int_number+1):
    if int_number%x == 0:
        list_count.append(x)
result = sum(list_count)
print(result)