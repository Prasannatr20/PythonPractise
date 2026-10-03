import random
num = random.randint(1,100)

i=0
while i<=4:
    nums = int(input("Enter a number: "))
    if nums==num:
        print("Correct!")
        break
    elif nums>num:
        print("High")
    else:
        print("Low")
    i+=1
else:
    print("You ran out of attempts")
    print("Guessed number is:",num)