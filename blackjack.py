from cards import Deck

# TODO: implement betting
# TODO: splitting pairs
# TODO: doubling down
# TODO: insurance 
class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.player_hand, self.dealer_hand = [], []

    def _get_card_type(self, card):
        '''
        returns the blackjack type of a card (Ace, Face, or Number)
        '''
        rank = card.get_rank_value()
        if rank == 14:
            return 'Ace'
        elif 14 > rank > 10:
            return 'Face'
        else:
            return 'Number'

    def deal(self):
        self.player_hand, self.dealer_hand = self.deck.deal_hands(2, 2)
        print('Player hand: {}'.format(self.player_hand))
        print('Dealer hand: [{}, {}]'.format(self.dealer_hand[0], "🂠"))

    def check_player_natural(self):
        '''
        checks if player has a natural blackjack
        '''
        if (self._get_card_type(self.player_hand[0]) == 'Ace' and self._get_card_type(self.player_hand[1]) == 'Face') or \
            (self._get_card_type(self.player_hand[0]) == 'Ace' and self._get_card_type(self.player_hand[1]) == 'Number'):
            print('Player has a natural blackjack!')
            return True
        else:
            return False

    def check_dealer_natural(self):
        '''
        checks if dealer has a natural blackjack
        '''
        if (self._get_card_type(self.dealer_hand[0]) == 'Ace' and self._get_card_type(self.dealer_hand[1]) == 'Face') or \
            (self._get_card_type(self.dealer_hand[0]) == 'Ace' and self._get_card_type(self.dealer_hand[1]) == 'Number'):
            print('Dealer has a natural blackjack!')
            return True
        else:
            return False

    def run(self):
        self.deal()

        player_natural = self.check_player_natural()
        dealer_natural = self.check_dealer_natural()

        self.play_hand()

if __name__ == '__main__':
    game = Blackjack()
    game.run()