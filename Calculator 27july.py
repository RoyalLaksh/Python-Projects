#calculator

print("Simple Calculator")
print("Options:+, -, *, /")
num1=float(input("please write your first number"))
operation=input("input any given option")
num2=float(input("please write your second number"))
if operation == "+":
        result=num1+num2

elif operation == "-":
        result=num1-num2
elif operation == "*":
        result=num1*num2
elif operation == "/":
        result=num1/num2
else:
        result="invalid operation"

print(result)
