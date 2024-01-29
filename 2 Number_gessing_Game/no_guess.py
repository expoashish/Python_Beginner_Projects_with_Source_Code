import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 to 100")
    secret_number = random.randint(1,100)
    attempt =0
    while True:
        try:
            guess = int(input("Enter your guess:"))
            attempt+=1
            if guess < secret_number:
                print("Too Low! try again")
            elif guess > secret_number:
                print("Too High! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
                break
        except:
            print("Invalid input")

if __name__=="__main__":
    number_guessing_game()