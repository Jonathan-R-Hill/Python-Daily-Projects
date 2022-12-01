# Variables

name = "Jonathan"

feet = 6
inch = 2

stones = 14
pounds = 6

# Covert height into inches and meters

feet_inch = feet * 12
total_height = feet_inch + inch

meters = total_height / 39.37

# Convert weight into pounds then kilos

stone_pound = stones * 14
total_pound = stone_pound + pounds

kilos = total_pound / 2.205

# Calculate BMI and check if you are a healthy weight     BMI = kg/m2 

bmi = round((kilos / (meters**2)), 2)

def bmi_calc(bmi):
    if bmi < 18.5:
        print(f"Your BMI is: {bmi}. You are under weight")

    elif bmi >=18.5 and bmi < 24.9:
        print(f"Your BMI is: {bmi}. You are a healthy weight")

    elif bmi > 25 and bmi < 30:
        print(f"Your BMI is: {bmi}. You are over weight")

    elif bmi > 30:
        print(f"Your BMI is: {bmi}. You are obease")


print(f"Hi {name}\nYour height is: feet: {feet} inches: {inch}\nYour weight is: St: {stones} P: {pounds}\n")
bmi_calc(bmi)
