str_cycle = input()
cycle = int(str_cycle)


for x in range(cycle) :
    str_repeat, str_text =input().split()
    repeat = int(str_repeat)
    text = list(str_text)
    list_new=[]
    for y in range(len(text)) :
        for z in range(repeat) :
            list_new.append(text[y])
    result = "".join(list_new)
    print(result)