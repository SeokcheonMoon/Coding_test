str_first,str_second = input().split()

first = list(str_first)
second = list(str_second)
first.reverse()
second.reverse()

str_reverse_first = "".join(first)
str_reverse_second = "".join(second)
reverse_first = int(str_reverse_first)
reverse_second = int(str_reverse_second)
pass

if reverse_first > reverse_second :
    answer = reverse_first
else :
    answer = reverse_second

print(answer)