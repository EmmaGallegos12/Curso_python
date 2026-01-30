"""
Tic Tac Toe Game
Author: José Emmanuel Gallegos Mazariego
"""

from game_logic import two_players
from game_logic import game
from menu import display_menu


def main():
    """
    main function to run the Tic Tac Toe game
    """
    while True:
        choice = display_menu()
        if choice == 1:
            print("One Player Game is not implemented yet.")
        elif choice == 2:
            two_players()
        elif choice == 3:
            print("Exiting the game. Goodbye!")
            break

if __name__ == "__main__":
    main()          