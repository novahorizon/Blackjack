from Shoe import *
import random
import abc

class PLAYER(abc.ABC):
    # 0 = hit, 1 = stand
    # 2 = doubleHit, 3 = doubleStand
    # 4 = split, 5 = double
    hard = [
        [],[],[],[], # 0 - 3
        [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 4
        [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 5
        [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 6
        [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 7
        [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 8
        [-1, -1, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0], # 9
        [-1, -1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0], # 10
        [-1, -1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], # 11
        [-1, -1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], # 12
        [-1, -1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], # 13
        [-1, -1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], # 14
        [-1, -1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], # 15
        [-1, -1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], # 16
        [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], # 17
        [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 18
        [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 19
        [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 20
        [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]  # 21
    soft = [
        [],[],[],[],[],[],[],[],[],[],[],[],[], # 0 - 12
        [-1, -1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],  # 13
        [-1, -1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],  # 14
        [-1, -1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0],  # 15
        [-1, -1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0],  # 16
        [-1, -1, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0],  # 17
        [-1, -1, 3, 3, 3, 3, 3, 1, 1, 0, 0, 0],  # 18
        [-1, -1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1],  # 19
        [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 20
        [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]  # 21
    splits = [
        [],[],[],[],
        [-1, -1, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0], [],  # 2,2
        [-1, -1, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0], [],  # 3,3
        [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [],  # 4,4
        [-1, -1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0],  # 5,5
        [-1, -1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # A,A
        [-1, -1, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0], [],  # 6,6
        [-1, -1, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0], [],  # 7,7
        [-1, -1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [],  # 8,8
        [-1, -1, 4, 4, 4, 4, 4, 1, 4, 4, 1, 1], [],  # 9,9
        [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [], # 20

    ]


    def __init__(self):
        self.hands = []
        self.activeHand = 0
        self.wins = 0
        self.total = 0

    def addCard(self, card):
        if len(self.hands) == 0:
            self.hands.append(HAND(card))
            self.activeHand = 0
        else:
            self.hands[self.activeHand].addCard(card)

    def endRound(self, dealervalue):
        for hand in self.hands:
            self.total += 1
            if (dealervalue < hand.total < 22) or (dealervalue > 21 and hand.total < 22):
                self.wins += 1
        self.hands = []
        self.activeHand = 0

    def finalize(self, action):
        if action == 2 or action == 3:
            if len(self.hands[self.activeHand].cards) == 2 and len(self.hands) == 1:
                return 5
            else:
                return action - 2
        return action

    def play(self, dealervalue, shoe: SHOE):
        while self.activeHand < len(self.hands):
            hand = self.hands[self.activeHand]
            act = -1
            while act != 1:
                if hand.total > 21:
                    act = 1
                else:
                    act = self.decide(dealervalue, shoe)
                if act == 0:
                    self.addCard(shoe.getcard())
                elif act == 4:
                    self.hands.append(HAND(hand.split()))
                    self.addCard(shoe.getcard())
                elif act == 5:
                    self.addCard(shoe.getcard())
                    act = 1
            self.activeHand += 1

    @abc.abstractmethod
    def decide(self, dealervalue, shoe: SHOE):
        # This method will only be used from subclasses but is referenced in the parent class method play()
        # Thus we shall just leave it blank
        raise NotImplementedError("Must implement in child class")






class PERFECT(PLAYER):
    # This player will perform the perfect decision as outlined in the parent class grids.
    def __init__(self):
        super().__init__()

    def decide(self, dealervalue, shoe):
        # 0 = hit, 1 = stand
        # 2 = doubleHit, 3 = doubleStand
        # 4 = split, 5 = double
        hand = self.hands[self.activeHand]
        act = -1
        if len(hand.cards) == 1: # if you only have 1 card, get a card. This happens on a new hand after a split
            self.addCard(shoe.getcard())
        if hand.canSplit and len(self.hands) < 4:
            # A,A has the same value as 6,6 so we have to check whether we have aces or just a standard value
            if hand.cards[0].value == 11:
                act = self.splits[11][dealervalue]
            else:
                act = self.splits[hand.total][dealervalue]
        elif not hand.isHard:
            act = self.soft[hand.total][dealervalue]
        else:
            act = self.hard[hand.total][dealervalue]
        return self.finalize(act)


class RAND(PLAYER):
    # this player will choose a legal action at random.
    def __init__(self):
        super().__init__()

    def decide(self, dealervalue, shoe):
        # for consistency with other subclasses of the same parent, dealervalue
        # is still requested, though it's not actually used by this subclass.
        # 0 = hit, 1 = stand
        # 2 = doubleHit, 3 = doubleStand
        # 4 = split, 5 = double
        hand = self.hands[self.activeHand]
        act = -1
        if hand.canSplit:
            act = random.randint(0,4)
        act = random.randint(0,3)
        return self.finalize(act)


