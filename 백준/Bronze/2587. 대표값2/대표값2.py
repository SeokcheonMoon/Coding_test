list_number = []
for x in range(5):
    number = int(input())
    list_number.append(number)
list_number.sort(reverse = False)
print(int(sum(list_number)/5))
print(list_number[2])