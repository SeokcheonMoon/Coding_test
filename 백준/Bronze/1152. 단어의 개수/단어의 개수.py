str_text = input()

text = list(str_text)


if text[0] ==" " and text[len(text)-1] == " " :
    count_blank = text.count(" ")-1
elif text[0] ==" " or text[len(text)-1] == " " : 
    count_blank = text.count(" ")
else :
    count_blank = text.count(" ")+1

print(count_blank)