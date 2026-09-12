import random

def guess_the_number():
    while True:
        secret_number = random.randint(1, 100)
        
        print("\n==========================================")
        print("Welcome to Guess the Number!")
        print("I'm thinking of a number between 1 and 100.")
        print("Can you guess it? (You only get ONE try!)")
        print("==========================================")
        
        user_input = input("Enter your guess: ")
        
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue
            
        guess = int(user_input)
        
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it right!")
            print(f"The secret number was indeed {secret_number}!")
        else:
            print(f"\n❌ Wrong guess! Game over.")
            print(f"The secret number was {secret_number}.")
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! See you next time.")
            break

if __name__ == "__main__":
    guess_the_number()