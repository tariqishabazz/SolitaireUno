import random  # Import the 'random' module for shuffling the cards

# Import the necessary elements from the 'Card' module
from Card import Values, Suits, Card  # Assumes Values, Suits (Enums), and Card class are defined there


class Deck:
    """
    Represents a standard deck of cards for a card game.
    It initializes with a full set of shuffled cards and allows dealing.
    """

    def __init__(self):
        """
        Initializes a new deck of 52 playing cards.
        Cards are created from all possible Values and Suits, then shuffled.
        """
        self.cards = []  # The list to hold all the Card objects in the deck

        # Loop through all defined card Values (e.g., Ace, Two, King)
        for value in Values:
            # For each Value, loop through all defined Suits (e.g., Diamonds, Clubs)
            for suit in Suits:
                # Create a new Card object with the current value and suit, and add it to the deck
                self.cards.append(Card(value, suit))

        random.shuffle(self.cards)  # Randomly arrange the cards in the deck

        #removing the Queen of Spades and placing at a random spot within deck for penalty rules
        penalty_card = Card(Values.Queen, Suits.Spades)
        self.cards.remove(penalty_card)

        random_position = random.randint(5, 27)
        self.cards.insert(random_position, penalty_card)

    def __len__(self):
        """
        Allows using the len() function on a Deck object (e.g., len(my_deck)).
        This also makes the Deck object 'truthy' (True if it has cards, False if empty)
        when used in a boolean context (e.g., 'if my_deck:').
        """
        return len(self.cards)  # Returns the number of cards currently in the deck

    def deal_card(self):
        """
        Removes and returns the top card from the deck.
        Handles the case where the deck is empty.
        """
        if len(self.cards) == 0:
            # If there are no cards left in the deck, return an informative message
            return "There are no cards left!"
        else:
            # Use .pop() to remove and return the last card from the list (which acts as the 'top' after shuffling)
            return self.cards.pop()
