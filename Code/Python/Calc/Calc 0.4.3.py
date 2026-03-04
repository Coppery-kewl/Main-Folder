#Copp CALC 0.4.3 by coppery
#Changelog
#Uses f strings now
#has modules and floors
version="0.4.3"

print(f"""Welcome to Calc {version} by coppery!!!
this version has addition, subtraction, multiplication, division, floor division, and powers!
i hope you use this well :]""")
input("Press ENTER to start")

print("Equation 1 Addition")
add1=input("Give the first number: ")
add2=input("Give the second number: ")
addsol=float(add1) + float(add2)
print(f"""Equation: {add1} + {add2}
      solution: {str(addsol)}""")
input("Press ENTER to continue")

print("Equation 2 Subtraction")
sub1=input("Give the first number: ")
sub2=input("Give the second number: ")
subsol=float(sub1) - float(sub2)
print(f"""Equation: {sub1} - {sub2}
      solution: {str(subsol)}""")
input("Press ENTER to continue")

print("Equation 3 Multiplication")
mult1=input("Give the first number: ")
mult2=input("Give the second number: ")
multsol=float(mult1) * float(mult2)
print(f"""Equation: {mult1} * {mult2}
      solution: {str(multsol)}""")
input("Press ENTER to continue")

print("Equation 4 Division")
div1=input("Give the first number: ")
div2=input("Give the second number: ")
divsol=float(div1) / float(div2)
print(f"""Equation: {div1} / {div2}
      solution: {str(divsol)}""")
input("Press ENTER to continue")

print("Equation 5 Floor Division (Rounds up decimals)")
flr1=input("Give the first number: ")
flr2=input("Give the second number: ")
flrsol=float(flr1) // float(flr2)
print(f"""Equation: {flr1} // {flr2}
      solution: {str(flrsol)}""")
input("Press ENTER to continue")

print("Equation 6 Powers (^)")
pow1=input("Give the first number: ")
pow2=input("Give the second number: ")
powsol=float(pow1) ** float(pow2)
print(f"""Equation: {pow1} ^ {pow2}
      solution: {str(powsol)}""")
input("Press ENTER to end")

print(f"Thanks for using Calc {version}!!!! You're pretty :3")
