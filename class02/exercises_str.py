# %%
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

name: str = input("Type your name: ")

print(f"{name.title()}")




# %%
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.


name: str = input("Type your name: ")

print(f"{name.upper()}")


# %%
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

no_space: str = input("Type a phrase: ")

print(f"{no_space.lstrip().rstrip()}")

# %%
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
date_input: str = input("Please enter a date (dd/mm/yyyy): ")

date_components = date_input.split('/')

if len(date_components) == 3:
    day = date_components[0]
    month = date_components[1]
    year = date_components[2]

    print(f"Day: {day}")
    print(f"Month: {month}")
    print(f"Year: {year}")
else:
    print("Error: Invalid date format. Please use the dd/mm/yyyy format.")


# %%
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

str1: str = input("Type your first str: ")
str2: str = input("Type your second str: ")

print(f"{str1+str2}")