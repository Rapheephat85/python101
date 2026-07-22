weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

print("Your BMI is: ", format(weight/((height/100)**2), ".2f"))

