weight = float(input("Enter weight in kg: "))
height = float(input("Entar height in meters: "))

bmi = weight/(height*height)

if bmi<18.5:
    print("Under weight")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal")
elif bmi>=25 and bmi<29.9:
    print("Overweight")
else:
    print("Obese")