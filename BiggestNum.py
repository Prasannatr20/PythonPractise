a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if(a>b and a>c):
    print(a, "is tyhe biggest nmber amon three")
elif(b>c):
    print(b, "is the greatest among three")
else:
    print(c, "is the greatest among three")