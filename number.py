import random

def guessing_game():
    # The computer picks a secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    while True:
        user_input = input("Take a guess: ")
        
        # Ensure the player typed a valid number
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue
            
        guess = int(user_input)
        attempts += 1

        # Check the player's guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You found the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()
