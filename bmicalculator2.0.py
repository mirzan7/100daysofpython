height = float(input("Enter your height in meter"))
weight = int(input("enter your weight in kg"))
bmi = weight/(height**2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obesce")
else:
    print("Clinically obesce")