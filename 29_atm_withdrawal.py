balance = int(input("Enter your balance amount: "))
withdraw = int(input("Enter your withdrawal amount: "))

if balance>0 and balance>= withdraw:
    print("Amount successfull withdrawn")
    print("Balance->",balance-withdraw)
else:
    print("Enter a valid balance or withdrawal amount")