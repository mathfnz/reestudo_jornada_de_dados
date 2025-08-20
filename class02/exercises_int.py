# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

#1
# %%
def calculate_sum(number1: int, number2: int) -> int:
    """
    function to sum two numbers: number1 (int) and number2 (int) and return result(int)
    """
    return number1 + number2

def main() -> None:

    try:
        n1: int = int(input("Type the first number: "))
        n2: int = int(input("Type the second number: "))

        calculated = calculate_sum(number1=n1, number2=n2)
        
        print(f"{n1} + {n2} = {calculated}")
        
        
    except ValueError as error:
        print(f"Key {error} is missing")
main()

# %%
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.


def calculate_rest (n1: int) -> int:
    """Calculates the remainder of a division of an integer by 5.

    Args:
        number (int): The integer to be divided (the dividend).

    Returns:
        int: The remainder of the division (number % 5).
    """
    return n1 % 5

def main2() -> None:
    try:
        number1: int = int(input(f"Type your number: "))
        
        rest: int = calculate_rest(n1=number1)
        print(f"{number1} / 5 has the remainder {rest}")
    except ValueError as ve:
        print(f"You have an error: {ve}")
        
main2()

# %%
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
def calculate_mult(n1: int, n2: int) -> int:
    return n1 * n2


def main3() -> None:
    try:
        number1: int = int(input("Type the first number: "))
        number2: int = int(input("Type the second number: "))
        mult: int = calculate_mult(n1=number1, n2=number2)
        
        print(f"{number1} * {number2} = {mult}")
    except ValueError as ve:
        print(f"You have an error: {ve}")

main3()





# %%
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

def calculate_div(n1: int, n2: int) -> int:
    return n1 // n2


def main4() -> None:
    try:
        number1: int = int(input("Type the first number: "))
        number2: int = int(input("Type the second number: "))
        div: int = calculate_div(n1=number1, n2=number2)
        
        print(f"{number1} // {number2} = {div}")
    except ValueError as ve:
        print(f"You have an error: {ve}")

main4()
# %%
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

def calculate_sqr(n1: int) -> int:
    return n1 ** 2


def main5() -> None:
    try:
        number1: int = int(input("Type the first number: "))
        sqrt: int = calculate_sqr(n1=number1)
        
        print(f"{number1} ˆ 2 = {sqrt}")
    except ValueError as ve:
        print(f"You have an error: {ve}")

main5()