# num = abs(int(input("Enter a number: ")))
# large = 0

# while(num!=0):
#     temp = num%10
#     if temp>large:
#         large = temp
#     num//=10
# print(large)


#Smallest

num = abs(int(input("Enter a number: ")))
small=9

while num!=0:
    temp = num%10
    if temp<small:
        small = temp
    num//=10
print(small)