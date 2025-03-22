"""
File: cards.py

Module for playing cards, with classes Card and Deck
""" 
import random

class Card(object):
    """ A card object with a suit, rank, and faceup status. """

    RANKS = tuple(range(1, 14))
    SUITS = ("Spades", "Diamonds", "Hearts", "Clubs")

    def __init__(self, rank, suit):
        """Creates a card with the given rank, suit, and face-down status."""
        self.rank = rank
        self.suit = suit
        self.faceup = False  # Default: card is face down

    def turn(self):
        """Flips the card (toggles faceup status)."""
        self.faceup = not self.faceup

    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = self.rank
        return f"{rank} of {self.suit} {self.faceup}"

class Deck(object):
    """ A deck containing 52 cards. """

    def __init__(self):
        """Creates a full deck of cards."""
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]

    def shuffle(self):
        """Shuffles the cards."""
        random.shuffle(self.cards)

    def deal(self):
        """Removes and returns the top card or None if the deck is empty."""
        return self.cards.pop(0) if self.cards else None

    def __len__(self):
        """Returns the number of cards left in the deck."""
        return len(self.cards)

    def __str__(self): 
        """Returns the string representation of a deck."""
        return "\n".join(str(card) for card in self.cards)

def main():
    """A simple test."""
    deck = Deck()
    
    # Print all cards face down
    print("A new deck, cards face down:")
    for card in deck.cards:
        print(card)
    
    # Shuffle deck
    deck.shuffle()
    
    # Turn all cards face up
    for card in deck.cards:
        card.turn()
    
    # Print all cards face up
    print("\nA deck shuffled once, cards face up:")
    for card in deck.cards:
        print(card)

if __name__ == "__main__":
    main()
