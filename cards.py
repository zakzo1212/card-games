from itertools import product
import random

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
    
    def __repr__(self) -> str:
        return self.__str__()
    
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
    
    def get_suit(self) -> str:
        return self.suit


class Deck:
    '''
    A mutable(?) deck of cards
    '''

    def __init__(self, with_jokers=False):
        
        # TODO: implement jokers

        self.deck = []
        for rank, suit in product(RANKS, SUITS):
            self.deck.append(Card(rank, suit))
        self._shuffle()

    def get_deck_len(self):
        return len(self.deck)

    def deal_hands(self, cards_per_hand: int, num_hands: int) -> list[list]:
        '''
        Returns a list of lists, where each tuple contains the cards for one of the hands. Deals 'num_hands' number
        of hands, each with 'cards_per_hand' cards

        cards_per_hand * num_hands < len(self.Deck)
        '''

        # TODO: CHANGE SO THAT DECK IS MODIFIED ON DEAL. DEALING CARDS SHOULD MEAN THAT THE DECK NO LONGER HAS THE 
        # DEALT CARDS

        if cards_per_hand * num_hands > len(self.deck):
            raise ValueError('Unable to deal {} hands with {} cards each because there are not enough cards in the deck'.format(
                num_hands, cards_per_hand
            ))
        
        hands = [[] for i in range(num_hands)]
        for i in range(cards_per_hand):
            for j in range(num_hands):
                # card_index = (num_hands * i) + j
                # hands[j].append(self.deck[card_index])
                hands[j].append(self.deal_next_card())
        return hands

    def _shuffle(self):
        random.shuffle(self.deck)

    def get_card_by_idx(self, idx: int) -> Card:
        if idx > len(self.deck) - 1:
            raise ValueError("Card indes out of range")
        
    def get_deck_state(self) -> list[Card]:
        
        ret = []
        for card in self.deck:
            card_rank = card.get_rank_value()
            card_suit = card.get_suit()
            ret.append(str(Card(card_rank, card_suit)))
        return ret
    
    def deal_next_card(self):
        # TODO: could just be easier to have the top of the deck be the first card in the deck. 
        return self.deck.pop()

        
        
