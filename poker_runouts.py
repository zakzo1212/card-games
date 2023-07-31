from cards import Deck
import itertools

class HeadsUpRunout:

    def __init__(self):
        self.deck = Deck()
        self.board = []

    def eval_hand_strength(self, hole):
        '''
        TODO: evaluate the strength of a hand by the end (find strenght of 7 cards combo)
        '''
        all_cards = hole + self.board
        best_strength = 0

        # Generate all possible combinations of 5 cards
        combinations = itertools.combinations(all_cards, 5)

        for combo in combinations:
            rank = self._eval_hand_strength(combo)
            if rank > best_strength:
                best_strength = rank

        return best_strength

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

    def _deal_flop(self):
        burn = self.deck.deal_next_card()
        for i in range(3):
            self.board.append(self.deck.deal_next_card())

    def _deal_turn(self):
        burn = self.deck.deal_next_card()
        self.board.append(self.deck.deal_next_card())

    def _deal_river(self):
        burn = self.deck.deal_next_card()
        self.board.append(self.deck.deal_next_card())

    def get_curr_board(self):
        return self.board
    
    def run(self):
        p1_hole, p2_hole = self.deck.deal_hands(cards_per_hand=2, num_hands=2)

        self._deal_flop()
        self._deal_turn()
        self._deal_river()

        p1_strength = self.eval_hand_strength(p1_hole)
        p2_strength = self.eval_hand_strength(p2_hole)

        print(p1_strength, p2_strength)


if __name__ == "__main__":
    game = HeadsUpRunout()
    game.run()
