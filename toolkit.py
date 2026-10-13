
# Python Week 8 - My Python Toolkit

# Tool 1: A calculator that performs basic arithmetic.
def simple_calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Choose an operation: +, -, *, /")
        operation = input("Enter operation: ").strip()

        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2
        elif operation == "*":
            answer = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Sorry, division by zero is not allowed.")
                return
            answer = num1 / num2
        else:
            print(f"Sorry, '{operation}' is not a valid operation.")
            return

        print(f"The answer is: {answer:g}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: A to-do list that allows tasks to be added, viewed, and removed.
def todo_manager():
    tasks = []

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' has been added.")
            else:
                print("Please enter a task.")

        elif choice == "2":
            if tasks:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your to-do list is empty.")

        elif choice == "3":
            task = input("Enter the task to remove: ").strip()

            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' has been removed.")
            else:
                print(f"Task '{task}' was not found.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print(f"Sorry, '{choice}' is not valid. Choose 1, 2, 3, or 4.")


# Tool 3: A guessing game that repeats until the correct number is guessed.
def number_guessing_game():
    secret_number = 7
    print("\n--- Number Guessing Game ---")
    print("Guess the secret number between 1 and 10!")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! The secret number was {secret_number}.")
                break

        except ValueError:
            print("Please enter a whole number.")


# Main program: Displays the menu and runs the selected tool.
def main():
    print("Welcome to My Python Toolkit!")

    while True:
        print("\nChoose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List Manager")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_manager()
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            print("Thank you for using My Python Toolkit. See you next time!")
            break
        else:
            print(
                f"Sorry, '{choice}' is not a valid choice. "
                "Please select 1, 2, 3, or 4."
            )


# Start the program.
if __name__ == "__main__":
    main()
