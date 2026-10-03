num = abs(int(input("Enter a number: ")))
prod=1

while num!=0:
    temp = num%10
    prod*=temp
    num//=10
print(prod)