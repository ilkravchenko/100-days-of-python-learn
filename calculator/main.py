from art import logo

play = True


def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

math_operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculation():
    print(logo)

    num1 = float(input("What is the first number?: "))

    for item in math_operations:
        print(item)

    operation = input("Pick an operator from the lines above: ")

    while play:
        num2 = float(input("What is the next number?: "))

        calculation_function = math_operations[operation]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        continue_play = input(f"Type 'y' to continue calculating with {result}, of type 'n' to exit.: ").lower()

        if continue_play == 'n':
            print("Goodbye")
            play = False
        elif continue_play == 'y':
            operation = input("Pick an operation: ")
            num1 = result
        else:
            print("You have typed unsuported character")
            continue

calculation()