#your code goes here
inp_weight = int(input("Enter your weight (in kgs)\n"))
inp_height = float(input("Enter your height (in meters)\n"))

calc = inp_weight/inp_height**2

if calc<=18.5:
    print("Underweight\n")

elif calc<=25:
    print("Normal\n")

elif calc<=30:
    print("Overweight\n")

elif calc>=30:
    print("Obesity\n")