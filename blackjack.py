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
    
    def _get_hand_value(self, hand):
        '''
        returns the value of a blackjack hand
        '''
        # TODO: handle aces potentially being 1 or 11
        value = 0
        for card in hand:
            rank = card.get_rank_value()
            if rank == 14:
                value += 11
            elif 14 > rank > 10:
                value += 10
            else:
                value += rank
        return value

    def deal(self):
        self.player_hand, self.dealer_hand = self.deck.deal_hands(2, 2)
        print('Player hand: {}'.format(self.player_hand))
        print('Dealer hand: [{}, {}]'.format(self.dealer_hand[0], "🂠"))

    def check_player_natural(self):
        '''
        checks if player has a natural blackjack
        '''
        if (self._get_card_type(self.player_hand[0]) == 'Ace' and self._get_card_type(self.player_hand[1]) == 'Face') or \
            (self._get_card_type(self.player_hand[1]) == 'Ace' and self._get_card_type(self.player_hand[0]) == 'Face'):
            print('Player has a natural blackjack!')
            return True
        else:
            return False

    def check_dealer_natural(self):
        '''
        checks if dealer has a natural blackjack
        '''
        if (self._get_card_type(self.dealer_hand[0]) == 'Ace' and self._get_card_type(self.dealer_hand[1]) == 'Face') or \
            (self._get_card_type(self.dealer_hand[1]) == 'Ace' and self._get_card_type(self.dealer_hand[0]) == 'Face'):
            print('Dealer has a natural blackjack!')
            return True
        else:
            return False
        
    def play_hand(self):
        '''
        plays the player's hand
        '''
        while True:
            if self.check_player_natural():
                break
            else:
                action = input('Hit or stand? (h/s) ')
                if action == 'h':
                    self.player_hand.append(self.deck.deal_next_card())
                    print('Player hand: {}'.format(self.player_hand))
                    if self._get_hand_value(self.player_hand) > 21:
                        print('Player busts!')
                        break
                else:
                    break

    def play_dealer_hand(self):
        '''
        plays the dealer's hand
        '''
        while True:
            if self.check_dealer_natural():
                break
            else:
                print('IN HERE')
                if self._get_hand_value(self.dealer_hand) < 17:
                    self.dealer_hand.append(self.deck.deal_next_card())
                    print('Dealer hand: {}'.format(self.dealer_hand))
                    if self._get_hand_value(self.dealer_hand) > 21:
                        print('Dealer busts!')
                        break
                else:
                    print('Dealer stands with {}'.format(self._get_hand_value(self.dealer_hand)))
                    break

    def run(self):
        self.deal()

        player_natural = self.check_player_natural()
        dealer_natural = self.check_dealer_natural()

        self.play_hand()
        self.play_dealer_hand()

if __name__ == '__main__':
    game = Blackjack()
    game.run()