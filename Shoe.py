import random


class CARD:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value


class DECK:
    def __init__(self):
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"] # These currently don't actually matter...
        faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards = []
        for s in suits:
            for i in range(13):
                self.cards.append(CARD(s, faces[i], values[i]))

    def shuffle(self):
        random.shuffle(self.cards)


class SHOE:
    def __init__(self):
        self.decks = []
        self.cards = []
        for i in range(6):
            self.decks.append(DECK())
            self.decks[i].shuffle()
            for j in range(52):
                self.cards.append(self.decks[i].cards[j])

    def shuffle(self):
        random.shuffle(self.cards)

    def getcard(self):
        return self.cards.pop()


class HAND:
    def __init__(self, card):
        self.cards = []
        self.cards.append(card)
        self.total = card.value
        self.canSplit = False
        if card.face == "A":
            self.hasAce = True
            self.isHard = False
        else:
            self.hasAce = False
            self.isHard = True

    def split(self):
        newcard = self.cards.pop(1)
        self.total = self.cards[0].value
        if self.cards[0].face == "A":
            self.hasAce = True
            self.isHard = False
        return newcard

    def addCard(self, card):
        self.cards.append(card)
        self.total += card.value
        if card.face == "A":
            self.hasAce = True
            if self.total <= 21:
                self.isHard = False
        else:
            self.hasAce = False
        if self.total > 21 and not self.isHard:
            self.total -= 10
            self.isHard = True
        if len(self.cards) == 2 and self.cards[0].value == self.cards[1].value:
            self.canSplit = True
        else:
            self.canSplit = False
