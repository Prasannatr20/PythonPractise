side1 = float(input("Enter side1 angle: "))
side2 = float(input("Enter side2 angle: "))
side3 = float(input("Enter side3 angle: "))

if side1+side2+side3==180:
    if side1==side2==side3:
        print("It is an Equilateral traingle")
    elif side1==side2 or side1==side3 or side2==side3:
        print("It is an Isosceles triangle")
    elif side1==90 or side2==90 or side3==90:
        print("It is a right angled traingle")
    else:
        print("It is a scalene triangle")
else:
    print("It is not a triangle")