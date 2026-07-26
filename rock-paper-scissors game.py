import random

items = ["rock", "paper", "scissors"]

print("====== ROCK PAPER SCISSORS ======")

while True:

    user = input("\nEnter rock/paper/scissors (or exit): ").lower()

    if user == "exit":
        print("Game Over!")
        break

    if user not in items:
        print("Invalid Choice!")
        continue

    computer = random.choice(items)

    print("Computer Choice:", computer)

    if user == computer:
        print("Match Draw!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("Congratulations! You Win.")

    else:
        print("Computer Wins!")