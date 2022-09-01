import art

def add(n1, n2):
    """ Adds two numbers and returns sum """
    return n1 + n2


def subtract(n1, n2):
    """ Subtracts two numbers and returns value """
    return n1 - n2


def multiple(n1, n2):
    """ Multiplies two numbers and returns value """
    return n1 * n2


def divide(n1, n2):
    """ divides two numbers and returns value """
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
}



def calculator():
    """main calculator code"""
    print(art.logo)
    pick_another_operation = True
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    while pick_another_operation:

        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Pick another number?: "))

        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        pick_another = input("Pick another number, press 'y'? n for new calculation ").lower()
        if pick_another == "y":
            num1 = answer
            continue

        else:
            pick_another_operation = False
            calculator()

calculator()