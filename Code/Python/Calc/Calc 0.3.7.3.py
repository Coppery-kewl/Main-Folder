#Copp Calc 0.3.7.3 by Coppery
ver="0.3.7.3"






print("Welcome to Calc " + ver + "!")
print("This version is quite simple. It supports only 2 numbers per equation :/")
print("However, it supports 4 operations (Addition, Subtraction, Multiplication and Division)! tho you might not need all so fill those not needed with 1")
print("WARNING: DIVIDING WITH ZERO NOT SUPPORTED YET AND WILL BREAK CODE.")

print("Equation 1 (Addition)")
plus1 = input("Give first number: ")
plus2 = input("Give second number: ")
print("First equation: " + plus1 + " + " + plus2)
plusAns=float(plus1) + float(plus2)
print("Ans: " + str(plusAns))

print("Equation 2 (Subtraction)")
minus1=input("Give first number: ")
minus2=input("Give second number: ")
print("Second equation: " + minus1 + " - " + minus2)
minusAns=float(minus1) - float(minus2)
print("Ans: " + str(minusAns))

print("Equation 3 (Multiplication)")
mult1=input("Give first number: ")
mult2=input("Give second number: ")
print("Third equation: " + mult1 + " * " + mult2)
multAns=float(mult1) * float(mult2)
print("Ans: " + str(multAns))

print("Equation 4 (Division)")
div1=input("Give first number: ")
div2=input("Give second number: ")
print("Fourth equation: " + div1 + " / " + div2)
divAns=float(div1) / float(div2)
print("Ans: " + str(divAns))

print("Thanks for using Calc " + ver + " <3 by Coppery :]")
