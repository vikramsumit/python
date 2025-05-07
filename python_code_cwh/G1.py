import random

# Define the choices
choices = ['Snake', 'Water', 'Gun']

# Rows: Player, Columns: Computer
#  0 = Draw, 1 = Player wins, -1 = Computer wins
matrix = [
#     S   W   G
    [0, 1, -1],  # S vs S,W,G
    [-1, 0, 1],  # W vs S,W,G
    [1, -1, 0]   # G vs S,W,G
]

def get_choice_index(choice):
    return choices.index(choice)

def print_result(player_choice, computer_choice, result):
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if result == 0:
        print("It's a draw!")
    elif result == 1:
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

def play_game():
    print("Welcome to Snake Water Gun Game!")
    print("Choices: Snake, Water, Gun")

    player_input = input("Enter your choice: ").capitalize()
    if player_input not in choices:
        print("Invalid choice. Try again.")
        return

    computer_choice = random.choice(choices)

    player_index = get_choice_index(player_input)
    computer_index = get_choice_index(computer_choice)

    result = matrix[player_index][computer_index]
    print_result(player_input, computer_choice, result)

play_game()
