def calculate_bonus(salary: float, percentage: float) -> float:
    """Calculates the bonus value from a salary and a percentage."""
    return (salary * percentage) / 100.0


def main() -> None:
    """Gathers user input, calculates total salary, and displays a summary."""
    name: str = input("Type your name: ")
    base_salary: float = float(input("Type your salary: "))
    bonus_percentage: float = float(input("Type your bonus in %: "))

    bonus_value = calculate_bonus(salary=base_salary, percentage=bonus_percentage)
    total_salary = base_salary + bonus_value

    print("\n--- Salary Summary ---")
    print(f"Employee: {name}")
    print(f"Base Salary:      ${base_salary:,.2f}")
    print(f"Bonus ({bonus_percentage}%): + ${bonus_value:,.2f}")
    print("--------------------------")
    print(f"Total Salary:     ${total_salary:,.2f}")


main()