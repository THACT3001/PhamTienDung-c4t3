height = float(input("Chiều cao?"))
weight = float(input("Cân nặng?"))
BMI = weight/(height**2)

print(BMI)

if BMI < 16:
    print("Severly underweight")
elif BMI >= 16 and BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 25:
    print("Normal")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
else:
    print("Obese")