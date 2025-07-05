z = "pain"
import sys
def OperatorFunc():
    global z
    if operation == "+":
        z = int(number1) + int(number2)
    if operation == "x" or "*":
        z = int(number1) * int(number2)
    if operation == "-":
        z = int(number1) - int(number2)
    if operation == "/":
        z = int(number1) / int(number2)
    if operation == "//":
        z = int(number1) // int(number2)
    if operation == "^":
        z = int(number1) ** int(number2)

 
def OperatorDisplayFunc():
    global x
    global y
    if operation == "+":
        x = "adding it to"
        y = "added to"
    if operation == "x" or "*":
        x = "multiplying it with"
        y = "multiplied by"
    if operation == "-":
        x = "Subtracting it from"
        y = "subtracted from"
    if operation == "/":
        x = "Dividing it by"
        y = "divided by"
    if operation == "//":
        x = "rDividing it by"
        y = "rdivided by"
    if operation == "^":
        x = "it to the power of"
        y = "to the power of"
sys.set_int_max_str_digits(0)

print("What do you want to calculate?")
number1 = input()
print(f"So we are taking {number1}")
print("How do you want to calculate these numbers?")
print("""Your options are: 
x or * for multiplication
- for subtraction
+ for addition
/ for division
// for remainder division
^ for exponentiation""")
operation = input()
OperatorDisplayFunc()
print("What other number are you using?")
number2 = input()
OperatorFunc()
print(x)
print ("Okay!")
print(f"Your equation is {number1} {y} {number2}")
print(f"Which equates to... {z}")
    





