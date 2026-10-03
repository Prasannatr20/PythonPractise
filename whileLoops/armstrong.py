num = abs(int(input("Enter a number: ")))
copy = num
count=0
ams=0

while copy!=0:
    count+=1
    copy//=10

copy=num

while copy!=0:
    temp = copy%10
    ams+=temp**count
    copy//=10
if ams==num:
    print("Amstrong")
else:
    print("Not an amstrong")