# Day - 7 -> Smart Calculator

def calculate(expression):
    return eval(expression)


while True:

    print("\n========== Smart Calculator ==========")
    print("1. Calculate Expression")
    print("2. Exit")
    print("======================================")

    choice = input("Enter your choice: ")

    match choice:

        # Calculate the entered expression
        case "1":
            expression = input("Enter expression: ")

            try:
                result = calculate(expression)
                print("Result:", result)

            except:
                print("Invalid expression!")

        # Exit the calculator
        case "2":
            print("Thank you for using the calculator!")
            break

        # Handle invalid menu choices
        case _:
            print("Invalid choice! Please enter 1 or 2.")