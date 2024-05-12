str_cycle = input()
cycle = int(str_cycle)

str_number = input()
number_list = list(map(int,(str_number)))

sum = 0
for x in range(cycle) :
    
    sum = sum + number_list[x-1]
print(sum)