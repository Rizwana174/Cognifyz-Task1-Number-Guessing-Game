import random
print("=" * 40)
print("      NUMBER GUESSING GAME")
print("=" * 40)
while True:
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    print("\nI have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == secret_number:
                print(f"\n🎉 Congratulations!")
                print(f"You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("📉 Too Low! Try Again.\n")
            else:
                print("📈 Too High! Try Again.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")
    else:
        print(f"\n😢 Game Over!")
        print(f"The correct number was {secret_number}")
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("\nThank you for playing!")
        break