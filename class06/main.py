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

