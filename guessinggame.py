import random


def play_game():
    print("Choose difficulty level:")
    print("1. Level 1 (1-10)")
    print("2. Level 2 (1-100)")
    print("3. Level 3 (1-1000)")
    difficulty = input("Enter 1, 2, or 3: ")

    if difficulty == '1':
        max_num = 10
    elif difficulty == '2':
        max_num = 100
    elif difficulty == '3':
        max_num = 1000
    else:
        print("Invalid choice. Defaulting to Medium (1-100).")
        max_num = 100

    number_to_guess = random.randint(1, max_num)
    attempts = 0
    guessed_correctly = False

    print(f"\nI have picked a number between 1 and {max_num}. Try to guess it!")

    while not guessed_correctly:
        user_guess = input("Enter your guess: ")

        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue

        user_guess = int(user_guess)
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            guessed_correctly = True


while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thanks you for playing my game! Goodbye and have a safe rest of your day!")
        break
