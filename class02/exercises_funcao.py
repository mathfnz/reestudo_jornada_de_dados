# %%
from typing import List
import math
#Calcular Média de Valores em uma Lista

def average_value(l: list[int]) -> float:
    avg = sum(l) / len(l)
    return avg 


def main() -> None:
    numbers_list: list = []
    numbers_list = [i for i in range(1, 1001, 10)]
    print(numbers_list)
    avg_list = average_value(l=numbers_list)
    print(avg_list)
if __name__ == "__main__":
    main()
    
# %%
# Converter Celsius para Fahrenheit em uma Lista

def celsius_to_fahrenheit(list_temperature: list[float]) -> list[float]:
    fahrenheit = [temperature * 1.8 + 32 for temperature in list_temperature]
    return fahrenheit

def main2() -> None:
    celsius: list = [33.8, 39, 27.8, 9, -2, 0, 11, 34, 24.8]
    result = celsius_to_fahrenheit(list_temperature=celsius)
    print(f"{result}")
if __name__ == "__main__":
    main2()