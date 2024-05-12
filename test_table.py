n= 3628800
result = 10


x = 1
while True:
    if int(n//x) == 0:
        
        n = n / x
        answer = x
        x = x+1
        print(answer)
    else :
        break