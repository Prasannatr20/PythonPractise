password = "Password@123"
i=0
j=3
while i <=2:
    j-=1
    pwd = input("Enter password: ")
    if pwd==password:
        print("Autheticated")
        break
    else:
        print("Wrong password, plase try again")
        print(j,"Chance(s) left")
    i+=1