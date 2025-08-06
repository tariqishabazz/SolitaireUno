from enum import Enum  # Import the Enum class to create enumerated types


# --- Card Enums ---
# Enums (enumerated types) are a set of symbolic names (members) bound to unique, constant values.
# They make your code more readable by using meaningful names instead of "magic numbers" (e.g., Suits.Diamonds instead of 0).

class Suits(Enum):
    """
    Defines the four standard suits for playing cards.
    Each suit is assigned an integer value (though the value itself isn't used for game logic).
    """
    Diamonds = 0
    Clubs = 1
    Hearts = 2
    Spades = 3


class Values(Enum):
    """
    Defines the standard ranks (values) for playing cards.
    Each rank is assigned its common numerical value, which is crucial for game logic (e.g., 2 < 3).
    Face cards (Jack, Queen, King) are assigned higher numerical values.
    """
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11  # Often assigned 11
    Queen = 12  # Often assigned 12
    King = 13  # Often assigned 13


# --- Card Class ---

class Card:
    """
    Represents a single playing card, combining a Value (rank) and a Suit.
    """

    def __init__(self, value: Values, suit: Suits):
        """
        Initializes a new Card object.

        Args:
            value (Values): The rank of the card (e.g., Values.Ace, Values.Two).
            suit (Suits): The suit of the card (e.g., Suits.Hearts, Suits.Spades).
        """
        self.value = value  # Stores the Value Enum member for the card's rank
        self.suit = suit  # Stores the Suit Enum member for the card's suit

    def __str__(self):
        """
        Returns a string representation of the Card.
        This is what gets displayed when printing a Card object (e.g., "Ace of Spades").
        """
        # Accesses the 'name' attribute of the Enum members (e.g., Values.Ace.name is "Ace")
        return f"{self.value.name} of {self.suit.name}"

    def __repr__(self):
        """
        Returns a developer-friendly string representation of the Card.
        This is primarily used for debugging and in list/container representations.
        Here, it reuses the __str__ representation for simplicity.
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Tells if this Card object is equal to another object.
        Two cards are considered equal if they have the same value AND the same suit.

        Required for Queen of Spades penalty
        """
        # First, check if the other object is even a Card instance
        if isinstance(other, Card):
            # If it is a Card, compare its value and suit to our own
            return self.value == other.value and self.suit == other.suit

        # If the other object is not a Card, they can't be equal, so return False
        return False

