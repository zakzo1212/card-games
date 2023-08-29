from cards import Deck
import itertools
import logging

class HeadsUpRunout:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.deck = Deck()
        self.board = []

    def eval_hand_strength(self, hole):
        '''
        given a list of cards, return the best possible hand strength and the cards that make up that hand
        '''
        all_cards = hole + self.board
        best_strength = 0
        best_cards = []

        # Generate all possible combinations of 5 cards
        combinations = itertools.combinations(all_cards, 5)

        for combo in combinations:
            rank = self._eval_hand_strength(combo)
            if rank > best_strength:
                best_strength = rank
                best_cards = combo
            elif rank == best_strength:
                best_strength = rank
                if not self._first_hand_better_kicker(best_cards, combo):
                    best_cards = combo

        return best_strength, best_cards
    
    def _first_hand_better_kicker(self, hand1, hand2):
        '''
        given two hands of the same rank, determine which hand is stronger
        '''
        hand1 = sorted(hand1, key=lambda card: card.get_rank_value())
        hand2 = sorted(hand2, key=lambda card: card.get_rank_value())
        for i in range(len(hand1)-1, -1, -1):
            if hand1[i].get_rank_value() > hand2[i].get_rank_value():
                return True
            elif hand1[i].get_rank_value() < hand2[i].get_rank_value():
                return False
        return True

    def _eval_hand_strength(self, hand):

        ranks = {
            'royal_flush': 10,
            'straight_flush': 9,
            'four_of_a_kind': 8,
            'full_house': 7,
            'flush': 6,
            'straight': 5,
            'three_of_a_kind': 4,
            'two_pair': 3,
            'one_pair': 2,
            'high_card': 1
        }

        suits = [card.get_suit() for card in hand]
        values = [card.get_rank_value() for card in hand]
        value_counts = {value: values.count(value) for value in set(values)}

        is_flush = len(set(suits)) == 1
        is_straight = len(set(values)) == 5 and max(values) - min(values) == 4

        if is_flush and is_straight:
            if max(values) == 14:  # Ace
                return ranks['royal_flush']
            else:
                return ranks['straight_flush']

        if max(value_counts.values()) == 4:
            return ranks['four_of_a_kind']

        if max(value_counts.values()) == 3 and len(value_counts) == 2:
            return ranks['full_house']

        if is_flush:
            return ranks['flush']

        if is_straight:
            return ranks['straight']

        if max(value_counts.values()) == 3:
            return ranks['three_of_a_kind']

        if list(value_counts.values()).count(2) == 2:
            return ranks['two_pair']

        if list(value_counts.values()).count(2) == 1:
            return ranks['one_pair']

        return ranks['high_card']
    
    def _get_hand_name(self, hand_strength):
        hand_names = {
            10: 'Royal Flush',
            9: 'Straight Flush',
            8: 'Four of a Kind',
            7: 'Full House',
            6: 'Flush',
            5: 'Straight',
            4: 'Three of a Kind',
            3: 'Two Pair',
            2: 'One Pair',
            1: 'High Card'
        }
        return hand_names[hand_strength]

    def _deal_flop(self):
        logging.info('Dealing the Flop:')
        burn = self.deck.deal_next_card()
        for i in range(3):
            self.board.append(self.deck.deal_next_card())
        logging.info('Flop comes {} {} {}'.format(self.board[0], self.board[1], self.board[2]))
        logging.info('BOARD: ' + str(self.get_curr_board()) + '\n')

    def _deal_turn(self):
        logging.info('Dealing the Turn:')
        burn = self.deck.deal_next_card()
        self.board.append(self.deck.deal_next_card())
        logging.info('Turn comes {}'.format(self.board[3]))
        logging.info('BOARD: ' + str(self.get_curr_board()) + '\n')

    def _deal_river(self):
        logging.info('Dealing the River')
        burn = self.deck.deal_next_card()
        self.board.append(self.deck.deal_next_card())
        logging.info('River comes {}'.format(self.board[4]))
        logging.info('BOARD: ' + str(self.get_curr_board()) + '\n')

    def get_curr_board(self):
        return self.board
    
    def run(self):
        p1_hole, p2_hole = self.deck.deal_hands(cards_per_hand=2, num_hands=2)

        logging.info('Player 1 hole cards: ' + str(p1_hole))
        logging.info('Player 2 hole cards: ' + str(p2_hole) + '\n')

        self._deal_flop()
        self._deal_turn()
        self._deal_river()

        p1_strength, p1_best_hand = self.eval_hand_strength(p1_hole)
        p2_strength, p2_best_hand = self.eval_hand_strength(p2_hole)

        logging.info('Player 1 best hand: ' + str(p1_best_hand))
        logging.info('Player 2 best hand: ' + str(p2_best_hand) + '\n')

        if p1_strength > p2_strength:
            logging.info('Player 1 wins with a {}!'.format(self._get_hand_name(p1_strength)))
        elif p1_strength < p2_strength:
            logging.info('Player 2 wins with a {}!'.format(self._get_hand_name(p2_strength)))
        else:
            if self._first_hand_better_kicker(p1_best_hand, p2_best_hand):
                logging.info('Player 1 wins with a {} due to better kicker!'.format(self._get_hand_name(p1_strength)))
            elif self._first_hand_better_kicker(p2_best_hand, p1_best_hand):
                logging.info('Player 2 wins with a {} due to better kicker!'.format(self._get_hand_name(p2_strength)))
            else:
                logging.info('Tie! Player 1 and Player 2 split the pot')


if __name__ == "__main__":
    game = HeadsUpRunout()
    game.run()
