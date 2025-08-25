# %%
# conversor de temperatura

def calculate_celsius_fahrenheit(c: float) -> float:
    """
    Calculates Fahrenheit temperature over celsius temperature
     Args:
        c (float): celsius temperature
    Returns:
        float: The calculated temperature
    """
    return (c * 1.8) + 32

def main() -> None:
    try:
        celsius: float = float(input("Type C temperature: "))
        fahrenheit: float = calculate_celsius_fahrenheit(c=celsius)
        print(f"{celsius} to fahrenheit: {fahrenheit:.2f}")
    except ValueError:
        print(f"Error: {ValueError}")
    
main()

# %%
# verificador de palíndromo

def is_padridrome(p: str) -> bool:
    """
    Verify if the character is palindrome
    Args: 
        str = the word choose to be verify
    Return:
        bool = True or False
    """
    x = p == p[::-1]
    if x is True:
        return True
    else:
        return False

def main2() -> None:
    
    try:
        palindromo: str = input("Type your word: ")
        x: bool = is_padridrome(p=palindromo)
        print({x})
    except ValueError:
        print(f"{ValueError}")
main2()