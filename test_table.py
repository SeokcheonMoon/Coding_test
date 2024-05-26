n=118372

number = str(n)
list_number = list(number)
list_number.sort(reverse=True)
answer = int("".join(list_number))
print(answer)