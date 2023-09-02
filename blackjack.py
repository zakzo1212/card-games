from cards import Deck
import logging
import time

# TODO: splitting pairs
# TODO: doubling down
# TODO: insurance 
# TODO: improve logging

class Outcome:
    TIE = 'tie'
    PLAYER_WIN = 'player_win'
    DEALER_WIN = 'dealer_win'

class Blackjack:

    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(message)s'
        )
        self.deck = Deck()
        self.player_hand, self.dealer_hand = [], []
        self.player_stack = 1000

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
        logging.info('\nPlayer hand: {}'.format(self.player_hand))
        logging.info('Dealer hand: [{}, {}]\n'.format(self.dealer_hand[0], "🂠"))

    def check_player_natural(self):
        '''
        checks if player has a natural blackjack
        '''
        if (self._get_card_type(self.player_hand[0]) == 'Ace' and self._get_card_type(self.player_hand[1]) == 'Face') or \
            (self._get_card_type(self.player_hand[1]) == 'Ace' and self._get_card_type(self.player_hand[0]) == 'Face'):
            logging.info('Player has a natural blackjack!')
            return True
        else:
            return False

    def check_dealer_natural(self):
        '''
        checks if dealer has a natural blackjack
        '''
        if (self._get_card_type(self.dealer_hand[0]) == 'Ace' and self._get_card_type(self.dealer_hand[1]) == 'Face') or \
            (self._get_card_type(self.dealer_hand[1]) == 'Ace' and self._get_card_type(self.dealer_hand[0]) == 'Face'):
            logging.info('Dealer has a natural blackjack!')
            return True
        else:
            return False
        
    def play_player_hand(self):
        '''
        plays the player's hand
        '''
        while True:
            if self.check_player_natural():
                return self._get_hand_value(self.player_hand)
            else:
                action = input('Hit or stand? (h/s) ')
                if action == 'h':
                    self.player_hand.append(self.deck.deal_next_card())
                    logging.info('Player hand: {}'.format(self.player_hand))
                    if self._get_hand_value(self.player_hand) > 21:
                        logging.info('Player busts!')
                        return self._get_hand_value(self.player_hand)
                else:
                    return self._get_hand_value(self.player_hand)
                
    def play_dealer_hand(self):
        '''
        plays the dealer's hand
        '''
        wait_time = 1
        logging.info('\nPlaying dealer hand...')
        logging.info('Dealer starting hand: {}'.format(self.dealer_hand))
        while True:
            time.sleep(wait_time)
            if self.check_dealer_natural():
                return self._get_hand_value(self.dealer_hand)
            else:
                if self._get_hand_value(self.dealer_hand) < 17:
                    logging.info('Dealer hits')
                    self.dealer_hand.append(self.deck.deal_next_card())
                    logging.info('Dealer hand: {}'.format(self.dealer_hand))
                    if self._get_hand_value(self.dealer_hand) > 21:
                        logging.info('Dealer busts!')
                        return self._get_hand_value(self.dealer_hand)
                else:
                    logging.info('Dealer stands with {}'.format(self._get_hand_value(self.dealer_hand)))
                    return self._get_hand_value(self.dealer_hand)

    def play_hand(self):
        '''
        plays the player's hand and the dealer's hand and determines the winner
        '''
        player_outcome = self.play_player_hand()

        if player_outcome > 21:
            logging.info('Dealer wins because player busted!')
            return Outcome.DEALER_WIN

        dealer_outcome = self.play_dealer_hand()

        logging.info('\n')

        if dealer_outcome > 21:
            logging.info('Player wins because dealer busted!')
            return Outcome.PLAYER_WIN
        elif player_outcome > dealer_outcome:
            logging.info('Player wins!')
            return Outcome.PLAYER_WIN
        elif dealer_outcome > player_outcome:
            logging.info('Dealer wins!')
            return Outcome.DEALER_WIN
        else:
            logging.info('Tie!')
            return Outcome.TIE

    def make_bet(self):
        '''
        makes a bet before the hand
        '''
        bet = int(input('Place your bet (current stack: {}): '.format(self.player_stack)))
        if bet > self.player_stack:
            logging.info('You do not have enough money to place that bet!')
            return self.make_bet()
        else:
            self.player_stack -= bet
        return bet

    def settle_bets(self, outcome, bet):
        '''
        settles bets after the hand
        '''
        if outcome == Outcome.PLAYER_WIN:
            self.player_stack += 2 * bet
        elif outcome == Outcome.TIE:
            self.player_stack += bet
        logging.info('Player stack: {}'.format(self.player_stack))

    def run(self):

        logging.info('Let\'s play some blackjack!')
        logging.info('Player starting stack: {}\n'.format(self.player_stack))

        while self.player_stack > 0:
            logging.info('\nDealing new hand...')
            bet = self.make_bet()
            self.deal()

            # player_natural = self.check_player_natural()
            # dealer_natural = self.check_dealer_natural()

            outcome = self.play_hand()
            self.settle_bets(outcome, bet)


if __name__ == '__main__':
    game = Blackjack()
    game.run()