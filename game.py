import random

# Diagrams for Rock, Paper, and Scissors
graphics = {
    0: """
       _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
    """,  # Rock
    1: """
       _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
    """,  # Paper
    2: """
       _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
    """  # Scissors
}

def determine_winner(player, computer):
    """
    Determine the winner based on the player's and computer's choices.
    :param player: Choice of the player (0: Rock, 1: Paper, 2: Scissors)
    :param computer: Choice of the computer (0: Rock, 1: Paper, 2: Scissors)
    :return: Result string
    """
    if player == computer:
        return "It's a tie!"
    elif (player == 0 and computer == 2) or \
         (player == 1 and computer == 0) or \
         (player == 2 and computer == 1):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
    
    try:
        player_choice = int(input("What's your choice? "))
        if player_choice not in [0, 1, 2]:
            raise ValueError("Invalid input. Please choose 0, 1, or 2.")
    except ValueError as e:
        print(e)
        return
    
    computer_choice = random.randint(0, 2)
    
    # Show the choices
    print(f"\nYou chose:\n{graphics[player_choice]}")
    print(f"The computer chose:\n{graphics[computer_choice]}")
    
    # Determine and display the result
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Run the game
play_game()
