# BMI Calculator (Height in Inches)

# Step 1: Get user input
weight = float(input("Enter your weight in kilograms: "))
height_in_inches = float(input("Enter your height in inches: "))

# Step 2: Convert height to meters (1 inch = 0.0254 meters)
height_in_meters = height_in_inches * 0.0254

# Step 3: Calculate BMI
bmi = weight / (height_in_meters ** 2)

# Step 4: Display result
print("\nYour BMI is:", round(bmi, 2))

# Step 5: Interpret result
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 24.9:
    print("You have a normal weight.")
elif bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
