num = abs(int(input("Enter a number: ")))
digit = abs(int(input("Enter a digit to find its occurance: ")))
count=0

while num!=0:
    temp = num%10
    if temp==digit:
        count+=1
    num//=10
print(count)