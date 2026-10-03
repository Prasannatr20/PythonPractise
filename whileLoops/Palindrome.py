num = int(input("Enter a number: "))
dummy = num
rev =0

while(dummy!=0):
    temp = dummy%10
    rev = rev*10+temp
    dummy = dummy//10

if rev == num:
    print("Palindrome")
else:
    print("Not a palindrome")