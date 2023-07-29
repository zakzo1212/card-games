from itertools import product

SUITS = {'spades', 'clubs', 'hearts', 'diamonds'}
RANKS = range(2, 15)

class Card:
    """
    An immutable playing card represented by it's rank and suit

    Rank must be an integer in the range 2 - 16, inclusive. Rank values 15 and 16 are the small and bigger joker, inclusive

    Suit must be one of 'spades', 'clubs', 'hearts', or 'diamonds'
    """

    def __init__(self, rank: int, suit: str, joker=None) -> None:

        # TODO: implement jokers

        if rank not in RANKS or suit.lower() not in SUITS:
            raise ValueError('Card with invalid values was attempted to be created')

        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return self._rank_str(self.rank) + ' of ' + self.suit
    
    def _rank_str(self, rank) -> str:
        face_cards = {
            11 : 'Jack', 
            12 : 'Queen', 
            13 : 'King', 
            14 : 'Ace'
        }
        if rank > 10:
            return face_cards[rank]
        else:
            return str(rank)
        
    def get_rank_value(self) -> int:
        return self.rank

    def get_rank_str(self) -> str:
        return self._rank_str(self.rank)


class Deck:
    '''
    A mutable(?) deck of cards
    '''

    def __init__(self, with_jokers=False):
        
        # TODO: implement jokers
        
        self.Deck = []
        for rank, suit in product(RANKS, SUITS):
            self.Deck.append(Card(rank, suit))

    def deal_hands(self, cards_per_hand: int, num_hands: int) -> list(tuple):
        '''
        Returns a list of tuples, where each tuple contains the cards for one of the hands. Deals 'num_hands' number
        of hands, each with 'cards_per_hand' cards

        cards_per_hand * num_hands < len(self.Deck)
        '''
        
