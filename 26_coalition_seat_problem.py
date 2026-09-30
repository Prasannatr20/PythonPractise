party1 = int(input("Enter no.of seats won: "))
party2 = int(input("Enter no.of seats won: "))
party3 = int(input("Enter no.of seats won: "))
majorityreq = 117

if(party1+party2+party3==234):
    if(party1>majorityreq):
        print("party1 is the ruling party")
    elif(party2>majorityreq):
        print("party2 is the ruling party")
    elif(party3>majorityreq):
        print("party3 is the ruling party")
    elif(party1+party2>majorityreq or party1+party3>majorityreq or party2+party3>majorityreq):
        print("coalition possible")
else:
    print("Enter a valid number of seats")