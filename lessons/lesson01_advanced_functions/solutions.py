def add (a: int , b: int) -> int:
    """ Add two numbers """
    return a + b

def subtract (a: int , b: int) -> int:
    """ Subtract two numbers """
    return a - b

def multiply (a: int , b: int) -> int:
    """ Multiply two numbers """
    return a * b

def divide (a: int , b: int) -> float:
    """ Divide two numbers """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
    

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

def calculate(operation: str, a: int, b: int) -> float:
    """ dispatch based on the operation and return result """
    try:
        return operations[operation](a, b)
    except KeyError:
        raise ValueError(f"Invalid operation: {operation}")
    except TypeError:
        raise ValueError(f"Invalid arguments: {a} and {b}")

if __name__ == "__main__":
    print(calculate("add", 1, 2))
    print(calculate("subtract", 1, 2))
    print(calculate("multiply", 1, 2))
    print(calculate("divide", 1, 2))
