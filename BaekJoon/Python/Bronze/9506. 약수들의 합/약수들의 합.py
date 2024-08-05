while True:
    str_number = input()
    number = int(str_number)

    if number == -1:
        break

    else:
        list_value = []
        for x in range(1,number):
            if number % x == 0:
                list_value.append(x)
        if sum(list_value) == number:
            list_answer = []
            for y in range(len(list_value)):
                list_answer.append(str(list_value[y]))
            answer = " + ".join(list_answer)
            print(f"{number} = {answer}")
        else:
            print(f"{number} is NOT perfect.")