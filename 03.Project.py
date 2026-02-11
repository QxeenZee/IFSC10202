# Prompt for the first number and convert to float
first_number = float(input("Enter First Number: "))

# Prompt for the operator
operator = input("Enter Operator (+,-,*,/): ")

# Prompt for the second number and convert to float
second_number = float(input("Enter Second Number: "))

# Check the operator and perform calculation
if operator == '+':
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif operator == '-':
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
elif operator == '*':
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif operator == '/':
    result = first_number / second_number
    print(f"{first_number} / {second_number} = {result}")
else:
    print("Invalid Operator")