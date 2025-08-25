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