number = int(input())
for x in range(number):
    value = int(input())
    first = value//25
    second = value%25//10
    third = value%25%10//5
    fourth = value%25%10%5//1
    print(f"{first} {second} {third} {fourth}")