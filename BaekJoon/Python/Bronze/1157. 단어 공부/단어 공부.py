str_text = input()
str_text = str_text.lower()
list_text = list(str_text)
list_unique = list(set(list_text))

list_count = []
for x in range(len(list_unique)):
    list_count.append(list_text.count(list_unique[x]))

if list_count.count(max(list_count))>=2:
    print("?")
else:
    index = list_count.index(max(list_count))
    print(list_unique[index].upper())