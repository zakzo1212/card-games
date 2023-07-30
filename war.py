from cards import Card, Deck
import logging

# START WITH NAIVE VERSION WHERE WINNER OF HAND IN CASE OF TIE IS PLAYER 1
# TODO: LOOK UP THE ACTUAL RULES OF WAR

def play_round(p1_hand, p2_hand):
    p1_card = p1_hand.pop()
    p2_card = p2_hand.pop()

    logging.basicConfig(level=logging.INFO)
    logging.info('Player 1 plays {} and Player 2 plays {}'.format(
        p1_card, p2_card
    ))

    if p1_card.get_rank_value() >= p2_card.get_rank_value():
        logging.info('Player 1 wins this round!\n')
        p1_hand = [p1_card, p2_card] + p1_hand
    else:
        logging.info('Player 2 wins this round!\n')
        p2_hand = [p1_card, p2_card] + p2_hand

    return [p1_hand, p2_hand]

def run():
    deck = Deck()
    p1_hand, p2_hand = deck.deal_hands(len(deck.get_deck_state()) // 2, 2)
    while len(p1_hand) > 0 and len(p2_hand) > 0:
        p1_hand, p2_hand = play_round(p1_hand, p2_hand)

        # TODO: add timeout 



if __name__ == "__main__":
    run()
