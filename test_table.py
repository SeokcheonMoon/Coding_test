n=123
answer = 6

str_number = str(n)
list_number = list(str_number)

sum=0
for x in range(len(list_number)):
    sum = sum+int(list_number[x])

print(sum)
