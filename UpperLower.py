char = ord(input("Enter a single character: "))

if char>=48 and char<=57:
    print("It is a digit")
elif char>=65 and char<=90:
    print("It is an upper case")
elif char>=97 and char<=122:
    print("It is  lower case")
elif char>=32 and char<=64:
    print("It is a special character")