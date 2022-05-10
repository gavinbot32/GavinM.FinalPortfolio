import card as cards
import commonGameFunctions as gf
class Hand(object):

    def __init__(self):
        self.cards = []

    @property
    def cards_total(self):
        return len(self.cards)

    def __str__(self):
        rep = ""
        if self.cards:
            for card in self.cards:
                rep += str(card)

        else:
            rep = "<EMPTY>"
        return rep

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def clear(self):
        self.cards.clear()


class Deck(Hand):

    def build_deck(self):
        for suit in cards.Card.SUITS:
            for rank in cards.Card.RANK:
                card = cards.Pos_card(rank, suit)
                self.add(card)

    def shuffle(self):
        import random
        random.shuffle(self.cards)


    def deal(self,hands_list,per_hand=1):
        cards_needed = len(hands_list) * per_hand
        if len(self.cards) >= cards_needed+ len(hands_list)*3:
            for rounds in range(per_hand):
                for hand in hands_list:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
        else:
            print("Not enough cards to deal")
            x = gf.askYorN("do you want to keep playing?")
            if x == "yes":
                for hand in hands_list:
                    hand.clear()
                self.clear()
                self.build_deck()
                self.shuffle()
                self.deal(hands_list,per_hand)
            else:
                return

if __name__ == "__main__":
    print("this is not a program try importing and using the classes")
    input("\n\nPress the enter key to exit")