# %%
# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
def calculate_sum(number1: float, number2: float) -> float:
    """Calculates the sum of two float numbers.
    Args:
        number1 (float): first number
        number2 (float): second number
    Returns:
        float: number1 + number2 = return.
    """
    return number1 + number2

def main() -> None:

    try:
        n1: float = float(input("Type the first number: "))
        n2: float = float(input("Type the second number: "))

        calculated = calculate_sum(number1=n1, number2=n2)
        
        print(f"{n1} + {n2} = {calculated}")
        
        
    except ValueError as error:
        print(f"Key {error} is missing")
main()


# %%
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

def calculate_average(n1: float, n2: float) -> float:
    """Calculates the average of two float numbers.
    Args:
        number1 (float): first number
        number2 (float): second number
    Returns:
        float: (number1 + number2) / 2 = return.
    """
    return (n1 + n2) / 2

def main2() -> None:
    try:
        number1: float = float(input("Type the first number: "))
        number2: float = float(input("Type the second number: "))
        
        avg_number = calculate_average(n1=number1, n2= number2)
        print(f"The average of {number1} and {number2} = {avg_number}")
    except ValueError as error:
        print(f"Error value: {error}")
main2()

# %%
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
import math

def calculated_power(b: float, e: float) -> float:
    """Calculates the power of two float numbers.
    Args:
        b (float): first number
        e (float): second number
    Returns:
        float: b ˆ e = return.
    """
    return pow(b, e)

def main3() -> None:
    try:
        base: float = float(input("Type your base: "))
        exponent: float = float(input("Type your exponent: "))
        
        power = calculated_power(b=base, e=exponent)
        print(f"{base} ^ {exponent} = {power}")
    except ValueError as error:
        print(f"Error: {error}")
main3()

# %%
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

def celsius_to_fahrenheit(c: float) -> float:
    """Calculates celsius in fahrenheit temperature.
    Args:
        c (float): celsius temperature
    Returns:
        (c * 1.8) + 32
    """
    return (c * 1.8) + 32

def main4() -> None:
    try:
        celsius: float = float(input("Type the temperature in Celsius: "))
        
        result: float = celsius_to_fahrenheit(c=celsius)
        print(f"{celsius}C = {result}F")
    except ValueError as error:
        print(f"Error: {error}")
    
main4()


# %%
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

def calculate_circle_area(r: float) -> float:
    """Calculates the circle area.
    Args:
        r (float): radius
    Returns:
        float: The calculated area of the circle.

    """
    if r < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (r ** 2)

def main5() -> None:
    try:
        radius: float = float(input("Type the radius: "))
        area = calculate_circle_area(r=radius)
        print(f"\nThe area of a circle with a radius of {radius} is approximately {area:.2f}.")
    except ValueError as error:
        print(f"Error: {error}")
    
main5()