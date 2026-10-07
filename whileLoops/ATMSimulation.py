exit = True
while exit:
    checkbalance= int(input("Enter you balance amount: "))
    deposit= int(input("Enter amount to deposit: "))
    withdraw= int(input("Enter withdraw amount: "))
    if checkbalance+deposit>=withdraw:
        print("Successfully withdrawn")
    else:
        print("Insuffcient amount")
    a=input("Want to exit? yes or no: ")
    if a== "yes":
        exit=False