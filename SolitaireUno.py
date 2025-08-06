# --- Solitaire Uno Game ---
# This script defines a simplified, turn-based version of Uno with ascending/descending rules.
# Players aim to get rid of all their cards by playing them in descending order or matching special conditions.

# Import necessary classes from other files
from BehindTheScenes import Deck  # Assumes Deck class handles deck creation, shuffling and dealing
from Card import Values, Suits, Card  # Assumes Card, Values (enums for ranks), and Suits (enums) are defined


class SolitaireUno:
    """
    Represents the Solitaire Uno game, managing the deck, player hands,
    game flow, and turn-based logic for a single-player vs. computer game.
    """

    # --- Game Methods ---
    # These are general utility methods for the game logic.

    @staticmethod
    def valid_card(potential_play: Card, currently_shown: Card) -> bool:
        """
        Validates if a 'potential_play' card can be played on 'currently_shown' card.
        Rules: Descending order (e.g., 5 on 6), or King on Ace (13 on 1).

        Args:
            potential_play (Card): The card the player/computer wants to play.
            currently_shown (Card): The card currently on the table.

        Returns:
            bool: True if the play is valid, False otherwise.
        """
        # Check if the potential card's value is exactly one less than the current card's value
        # We access the numerical value of the Enum member using '.value.value'
        if potential_play.value.value == currently_shown.value.value - 1:
            return True

        # Check for the special case: playing a King (13) on an Ace (1)
        elif potential_play.value.value == 13 and currently_shown.value.value == 1:
            return True

        # If neither of the above conditions are met, the card is not valid
        return False

    def __init__(self):
        """
        Initializes a new game of Solitaire Uno.
        Sets up the deck, deals cards to players, and reveals the first card on the table.
        """
        # Display the game introduction and rules
        print("\n--- Solitaire Uno --- \n"
              "A simplified, turn-based version of Uno with descending rules. \n"
              "Players will be dealt 10 cards. \n"
              "They must then place a card in descending order based on the card currently visible. \n"
              "Watch out for that pesky Queen of Spades!\n"
              "\nWhoever plays all their cards wins\n")

        # Create a new deck of cards
        self.gameDeck = Deck()
        # Initialize empty hands for the player and the computer
        self.playersHand = []
        self.computersHand = []

        # Deal 10 cards to the player's hand
        for i in range(10): 
            card = self.gameDeck.deal_card()  # Get a card from the deck
            self.playersHand.append(card)  # Add it to the player's hand

        # Deal 10 cards to the computer's hand
        for i in range(10):
            card = self.gameDeck.deal_card()
            self.computersHand.append(card)

        # Deal and display the first card to start the discard pile
        self.current_card = self.gameDeck.deal_card()
        print(f"\n       The first card is: {self.current_card}")

    def start_game(self):
        """
        Starts and manages the main gameplay loop of Solitaire Uno.
        Alternates turns between the player and the computer until one runs out of cards.
        """
        # Main gameplay loop: Continues as long as both players have cards
        while self.playersHand and self.computersHand:

            # --- Player's Turn Logic ---
            player_turn_finished = False

            # Loop until the player makes a valid move or chooses to pass/pickup
            while not player_turn_finished:

                # Display player's hand at the start of their turn
                print(f"\nHere is your hand:")
                for i, card in enumerate(self.playersHand):
                    print(f'   {i + 1}) {card}')

                print(f"\n       Card currently visible: {self.current_card}")  # Show current table card

                valid_choice = False

                # Loop until the player enters a valid input format
                while not valid_choice:
                    print('\nMake your move: (1 - highest number of cards, pickup, or pass is deck is empty)')
                    player_decision = input()  # Get player's input

                    # Check if the input is a number (meaning they want to play a card)
                    if player_decision.isnumeric():
                        decision_as_number = int(player_decision)  # Convert input to an integer

                        # Check if the chosen card number is within the bounds of their hand
                        if 1 <= decision_as_number <= len(self.playersHand):
                            valid_choice = True  # Input format is valid

                            # Validate the chosen card against the current card on the table
                            chosen_card = self.playersHand[decision_as_number - 1]  # Get the actual Card object
                            is_play_valid = self.valid_card(chosen_card, self.current_card)

                            # If the card is valid, execute the play
                            if is_play_valid:
                                print(f"\n       You played: {chosen_card}")
                                self.current_card = chosen_card  # Update the current card on the table
                                self.playersHand.remove(chosen_card)  # Remove the card from the player's hand
                                player_turn_finished = True  # Player's turn is over

                            else:
                                print('       Sorry, that play is not valid, please choose another card')

                        else:
                            print('       Sorry, that card number is not in your hand. Please try again.')


                    # Check if the player chose to 'pass'
                    elif player_decision == 'pass' or player_decision == 'Pass':

                        # only allows passing if there are no cards in deck
                        if not self.gameDeck:
                            print("\n       You passed")

                            player_turn_finished = True  # Player's turn is over
                            valid_choice = True  # Input format is valid

                        # if there are, don't allow passing
                        else:
                            print("\n       There are cards still in the deck. Pickup or Play!")

                    # Check if the player chose to 'pickup' a card
                    elif player_decision == 'pickup' or player_decision == 'Pickup' or player_decision == 'pick up':

                        # Check if there are cards left in the main deck to pick up
                        if self.gameDeck:  # Uses __len__ method of Deck to check if it's not empty
                            print("\n       You didn't play and picked up a card.")

                            new_card = self.gameDeck.deal_card()  # storing the drawn card in new_card for later verification

                            self.playersHand.append(new_card)  # Add new card to hand

                            # checks to see if the new card is the Queen of Spades...
                            if new_card == Card(Values.Queen, Suits.Spades):

                                # if so, inform of penalty
                                print("\n   You picked up the Queen of Spades, you received 5 additional cards")

                                # enforce penalty through adding additional cards to hand
                                if len(self.gameDeck) >= 5:
                                    for i in range(5):
                                        self.playersHand.append(self.gameDeck.deal_card())

                            player_turn_finished = True  # Player's turn is over
                            valid_choice = True  # Input format is valid

                        else:
                            print("\n       There are no more cards left in the deck! You must choose to play or pass.")
                            # Player needs to make another valid choice as the deck is empty

                    # If the input is not a number, 'pass', or 'pickup'
                    else:
                        print("\n       Sorry, that choice is invalid, please try again")

            # --- Computer's Turn Logic ---
            computer_played = False  # Flag to track if computer played a card

            # Computer tries to find a valid card to play
            for card in self.computersHand:

                # Check for standard descending play
                if self.valid_card(card, self.current_card):  # Using the valid_card method
                    print(f"\n       Computer Played: {card}")
                    self.current_card = card  # Update the current card on the table
                    self.computersHand.remove(card)  # Remove card from computer's hand

                    if len(self.computersHand) == 0:
                        print("\n\n       Computer played its last card!")

                    computer_played = True  # Computer successfully played
                    break  # Exit loop as a card has been played

            # If the computer couldn't find a card to play in its hand
            if not computer_played:

                # Check if there are cards in the deck for the computer to pick up
                if self.gameDeck:
                    print("\n       Computer couldn't play and picked up a card.")

                    new_card = self.gameDeck.deal_card()  # storing the drawn card in new_card for later verification

                    self.computersHand.append(new_card)  # Add new card to hand

                    # checks to see if the new card is the Queen of Spades...
                    if new_card == Card(Values.Queen, Suits.Spades):

                        # if so, inform of penalty
                        print("\n   The computer picked up the Queen of Spades, and received 5 additional cards")

                        # enforce penalty through adding additional cards to hand
                        if len(self.gameDeck) >= 5:
                            for i in range(5):
                                self.computersHand.append(self.gameDeck.deal_card())

                else:
                    print("\n       Computer couldn't play and has no cards to pick up, so it passed.")
                    # Computer is forced to pass

            # Optional: You might want to print the computer's hand length here for debugging/interest
            # print(f"Computer's hand size: {len(self.computersHand)}")

        # --- Game End Conditions ---
        # These checks run after the main gameplay loop (while loop) finishes.
        # This means one of the players has run out of cards.
        if len(self.computersHand) == 0:
            print("\n\nYou Lose! You've been bested by the machine :(")

        elif len(self.playersHand) == 0:
            print("\n\nYou Win! You beat the computer! Congrats! :)")


# --- Game Execution ---
# This block ensures the game only starts when the script is run directly,
# not when it's imported as a module into another script.
if __name__ == "__main__":
    game = SolitaireUno()  # Create an instance of the SolitaireUno game (this calls __init__)
    game.start_game()  # Start the main game loop
