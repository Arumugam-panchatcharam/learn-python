# 1. Everything is an object

def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"

number = 10
text = "hello"
items = [1, 2, 3]

print(type(number))
print(type(text))
print(type(items))
print(type(greet))

# functions can be assigned
say_hello = greet

print(greet("Alice"))
print(say_hello("Alice"))

# Functions can be stored
def square(x: int) -> int:
    return x * x


def cube(x: int) -> int:
    return x * x * x


operations = [square, cube]

for operation in operations:
    print(operation(3))

# functions can be passed
def greet(name: str) -> str:
    return f"Hello {name}"


def execute(func, value):
    print(func(value))


execute(greet, "Bob")

# functions can be returned
def choose(language: str):
    if language == "en":
        return str.upper

    return str.lower


formatter = choose("en")

print(formatter("python"))