from cards import Deck

class HeadsUpRunout:

    def __init__(self):
        self.deck = Deck()
        self.board = []

    def eval_hand_strength(self):
        '''
        TODO: evaluate the strength of a hand by the end (find strenght of 7 cards combo)
        '''
        pass

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


if __name__ == "__main__":
    game = HeadsUpRunout()
    game.run()
