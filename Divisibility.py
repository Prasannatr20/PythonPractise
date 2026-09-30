num = int(input("Enter a number: "))
if num%2==0 and num%3==0:
    print(num,"is divisible by both 2 and 3")
elif num%2==0:
    print(num, "is divisibile by 2 only")
else:
    print(num,"is divisible by 3 only")