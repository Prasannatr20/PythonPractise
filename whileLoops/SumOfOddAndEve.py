i =0
evenSum=0
oddSum=0
while i<=100:
    if i%2==0:
        evenSum+=i
    else:
        oddSum+=i
    i+=1
print(evenSum)
print(oddSum)