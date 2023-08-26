from cards import Card, Deck
import logging
import random
import time

class War:
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.deck = Deck()
        self.p1_hand, self.p2_hand = self.deck.deal_hands(self.deck.get_deck_len() // 2, 2)
        self.round = 0      
        self.round_delay_secs = 0.01

    def war(self, card_pool: list[Card] = []):
        if len(self.p1_hand) < 2:
            logging.info('Player 1 does not have enough cards to go to war!')
            self.p2_hand = card_pool + self.p2_hand
            return
        if len(self.p2_hand) < 2:
            logging.info('Player 2 does not have enough cards to go to war!')
            self.p1_hand = card_pool + self.p1_hand
            return

        p1_first, p1_second = self.p1_hand.pop(), self.p1_hand.pop()
        p2_first, p2_second = self.p2_hand.pop(), self.p2_hand.pop()
        card_pool += [p1_first, p1_second, p2_first, p2_second]

        logging.info('Player 1 plays {} and Player 2 plays {}'.format(
            p1_second, p2_second
        ))

        random.shuffle(card_pool)
        if p1_second.get_rank_value() > p2_second.get_rank_value():
            logging.info('Player 1 wins the war!')
            self.p1_hand = card_pool + self.p1_hand
        elif p1_second.get_rank_value() < p2_second.get_rank_value():
            logging.info('Player 2 wins the war!')
            self.p2_hand = card_pool + self.p2_hand
        else:
            self.war(card_pool)

    def play_round(self):
        self.round += 1
        logging.info('PLAYING ROUND {}'.format(self.round))

        p1_card = self.p1_hand.pop()
        p2_card = self.p2_hand.pop()

        logging.info('Player 1 plays {} and Player 2 plays {}'.format(
            p1_card, p2_card
        ))

        card_pool = [p1_card, p2_card]
        random.shuffle(card_pool)
        if p1_card.get_rank_value() > p2_card.get_rank_value():
            logging.info('Player 1 wins this round!')
            self.p1_hand = card_pool + self.p1_hand
        elif p1_card.get_rank_value() < p2_card.get_rank_value():
            logging.info('Player 2 wins this round!')
            self.p2_hand = card_pool + self.p2_hand
        else:
            logging.info('WAR!')
            self.war(card_pool=card_pool)

        logging.info('Player 1 now has {} cards'.format(len(self.p1_hand)))
        logging.info('Player 2 now has {} cards\n'.format(len(self.p2_hand)))

    def run(self):
        while len(self.p1_hand) > 0 and len(self.p2_hand) > 0:
            self.play_round()
            time.sleep(self.round_delay_secs)

if __name__ == "__main__":
    war_game = War()
    war_game.run()
