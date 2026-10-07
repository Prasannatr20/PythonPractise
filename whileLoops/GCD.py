a= abs(int(input("Enter a number: ")))
b= abs(int(input("Enter a number: ")))

# a= num1*q+r

while b!=0:
    a,b= b, a % b
print(a)