num = int(input("Enter a number: "))
large = 0

while(num!=0):
    temp = num%10
    if temp>large:
        large = temp
    num//=10
print(large)
