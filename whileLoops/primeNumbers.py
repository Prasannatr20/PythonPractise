i=2

while i<=50:
    count = 0
    j=2
    while j<=i//2:
        if i%j==0:
            count+=1
            break
        j+=1
    if count==0:
        print(i)
    i+=1