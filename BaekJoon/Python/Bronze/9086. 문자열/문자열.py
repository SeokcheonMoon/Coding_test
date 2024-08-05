str_cycle = input()
cycle = int(str_cycle)

for x in range(cycle) : 
    str_text = input()
    text_list = list(str_text)

    print("{}{}".format(text_list[0],text_list[len(text_list)-1]))