from math.operations import add, subtract, multiply, divide, power

def main():
    x = 10
    y = 5

    print(f"Addition: {x} + {y} = {add(x, y)}")
    print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
    print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
    print(f"Division: {x} / {y} = {divide(x, y)}")
    print(f"Power: {x} ** {y} = {power(x, y)}")

if __name__ == "__main__":
    main()