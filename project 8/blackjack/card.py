class Card(object):

    RANK = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["♣","♦","♥","♠"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = str.format("""
            ______________
            |{0}{1}          |
            |            |
            |            |
            |            |
            |            |
            |            |
            |            |
            |          {1}{0}|
            ______________
            
            
            
            """,self.rank,self.suit)

        return rep

    def flip(self):
        self.faceUp =  not self.faceUp

class Pos_card(Card):
    def __init__(self,rank,suit):
        super(Pos_card, self).__init__(rank,suit)
        self.faceUp = False

    def __str__(self):
        if self.faceUp:
            rep = super(Pos_card, self).__str__()
        else:
            rep = str.format("""
                       ______________
                       |            |
                       |            |
                       |            |
                       |            |
                       |            |
                       |            |
                       |            |
                       |            |
                       ______________



                       """)
        return rep


if __name__ == "__main__":
    print("this is not a program try importing and using the classes")
    input("\n\nPress the enter key to exit")