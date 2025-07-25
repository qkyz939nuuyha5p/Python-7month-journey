# mini project on rock,paper,scissors game
import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if user not in choices:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.")
        return "invalid"
    
    computer = random.choice(choices)

    print(f"You: {user}")
    print(f"Computer: {computer}")

    if user == computer:
        print("🤝 It's a tie!")
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You win this round!")
        return "user"
    else:
        print("💻 Computer wins this round!")
        return "computer"

# Main game loop
user_wins = 0
computer_wins = 0

while user_wins < 2 and computer_wins < 2:
    result = play_game()
    
    if result == "user":
        user_wins += 1
    elif result == "computer":
        computer_wins += 1
    elif result == "invalid":
        continue  # Do not count invalid round
    
    print(f"📊 Score: You {user_wins} - Computer {computer_wins}")

# Final match result
if user_wins > computer_wins:
    print("\n🔥 YOU WON THE BEST-OF-3 MATCH! 🔥")
else:
    print("\n❌ COMPUTER WON THE BEST-OF-3 MATCH! ❌")
