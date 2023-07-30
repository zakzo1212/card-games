from cards import Card, Deck
import logging
import random

# START WITH NAIVE VERSION WHERE WINNER OF HAND IN CASE OF TIE IS PLAYER 1
# TODO: LOOK UP THE ACTUAL RULES OF WAR
# TODO: does war sometime not conclude?

class War:
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.deck = Deck()
        self.p1_hand, self.p2_hand = self.deck.deal_hands(self.deck.get_deck_len() // 2, 2)

        self.round = 0        

    def play_round(self):
        self.round += 1
        logging.info('PLAYING ROUND {}'.format(self.round))

        p1_card = self.p1_hand.pop()
        p2_card = self.p2_hand.pop()

        logging.info('Player 1 plays {} and Player 2 plays {}'.format(
            p1_card, p2_card
        ))

        if p1_card.get_rank_value() >= p2_card.get_rank_value():
            logging.info('Player 1 wins this round!')
            self.p1_hand = [p1_card, p2_card] + self.p1_hand
        else:
            logging.info('Player 2 wins this round!')
            self.p2_hand = [p1_card, p2_card] + self.p2_hand

        # currently shuffling entire hand after every round. TODO: not really the right rules
        random.shuffle(self.p1_hand)
        random.shuffle(self.p2_hand)

        logging.info('Player 1 now has {} cards'.format(len(self.p1_hand)))
        logging.info('Player 2 now has {} cards\n'.format(len(self.p2_hand)))


    def run(self):

        while len(self.p1_hand) > 0 and len(self.p2_hand) > 0:
            self.play_round()
            # TODO: add timeout 



if __name__ == "__main__":
    war_game = War()
    war_game.run()
