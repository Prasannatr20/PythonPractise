greatestNum=None
smallestNum=None

while True:
    i = int(input("Enter a number: "))

    if i==-1:
        break
    if greatestNum==None or i>greatestNum:
        greatestNum=i
    if smallestNum==None or i<smallestNum:
            smallestNum=i
print(greatestNum)
print(smallestNum)