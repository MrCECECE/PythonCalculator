"""A simple console calculator that can perform addition, subtraction, multiplication and division operations."""

input_line = input("Enter an example: ")

action = ""
math_symbols = ["+", "-", "*", "/"]
numbers = [str(num) for num in range(0, 10)]
for symbol in input_line:
    if symbol in math_symbols:
        action = symbol
    elif symbol not in numbers:
        print(f"Input error: {symbol} - unknown character")
        exit()
if action == "":
    print("Error: you did not enter the action sign.")
    exit()
working_list = list(map(int, input_line.split(action)))

if action == "+":
    print(f"Answer: {working_list[0] + working_list[1]}.")
elif action == "-":
    print(f"Answer: {working_list[0] - working_list[1]}.")
elif action == "*":
    print(f"Answer: {working_list[0] * working_list[1]}.")
elif action == "/":
    if working_list[1] != 0:
        print(f"Answer: {working_list[0] / working_list[1]}.")
    else:
        print("Answer: The expression doesn't make sense (division by 0).")
