str_number = input()

def multiply(str_number) :
    
    number = int(str_number)
    for x in [1,2,3,4,5,6,7,8,9] :

        print("{} * {} = {}".format(number, x, number*x))
    
    return 

multiply(str_number)