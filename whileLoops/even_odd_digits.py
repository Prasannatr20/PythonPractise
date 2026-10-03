num = abs(int(input("Enter a number: ")))
even = 0
evenCount=0
odd = 0
oddCount=0
while num!=0:
    temp = num%10
    if temp%2==0:
        even+=temp
        evenCount+=1
    else:
        odd+=temp
        oddCount+=1
    num//=10
print("Even->",even,"count->",evenCount)
print("Odd->",odd,"Count->",oddCount)