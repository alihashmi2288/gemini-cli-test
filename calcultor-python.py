
import math

def scientific_calculator():
    """
    A scientific command-line calculator.
    """
    print("Welcome to the Scientific CLI Calculator!")
    print("Enter 'exit' to quit.")

    while True:
        try:
            expression = input("Enter an expression: ")

            if expression.lower() == 'exit':
                break

            # Replace common math functions with their math module equivalents
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('ln', 'math.log')
            expression = expression.replace('^', '**')
            expression = expression.replace('pi', 'math.pi')
            expression = expression.replace('e', 'math.e')

            result = eval(expression)
            print("Result:", result)

        except (SyntaxError, NameError, ZeroDivisionError) as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

if __name__ == "__main__":
    scientific_calculator()
