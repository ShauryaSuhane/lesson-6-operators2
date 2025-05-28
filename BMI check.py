height=float(input("what is your height:"))
weight=float(input("what is your weight:"))
BMI= height / (weight/100)**2
print("your BMI is",BMI)
if BMI<=18.5:
    print("You are underweight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are over weight")
elif BMI<=34.9:
    print("you are severarily overweight")
elif BMI<=39.9:
    print("you are obese")
else:
    print("you are severarily obese")