username="admin"
password="1234"

usn = input("Enter username: ")
pwd = input("Enter password: ")

if(usn==username and pwd == password):
    print("Logged in successfully")
else:
    print("Invalid username or password")