from Shoe import *
from Player import *
import time
from multiprocessing import Process, Queue


start = time.time()

def rungames(q):
    shoe = SHOE()
    players = [PERFECT(), RAND()]
    shoe.shuffle()
    for _ in range(50000):

        myhand = None
        if len(shoe.cards) < 50:
            shoe = SHOE()
            shoe.shuffle()
        for player in players:
            player.addCard(shoe.getcard())
        myhand = HAND(shoe.getcard())
        for player in players:
            player.addCard(shoe.getcard())
        myhand.addCard(shoe.getcard())

        for player in players:
            player.play(myhand.cards[0].value, shoe)

        finished = False
        while not finished:
            if myhand.total < 17:
                myhand.addCard(shoe.getcard())
            elif myhand.total == 17 and not myhand.isHard:
                myhand.addCard(shoe.getcard())
            else:
                finished = True
        for player in players:
            t = []
            for h in player.hands:
                t.append(h.total)
            m = myhand.total
            player.endRound(myhand.total)
    # print("----")
    # for p in players:
    #     print(f"{p.wins / p.total * 100}")
    q.put(players[0].wins / players[0].total * 100)

if __name__ == '__main__':

    q = []
    p = []
    results = []
    start = time.time()
    workers = 500
    for i in range(workers):
        q.append(Queue())
        p.append(Process(target=rungames, args=(q[i],)))
        p[i].start()
        print(f"starting process {i}")
    for i in range(workers):
        results.append(q[i].get())
        p[i].join()

    # q = Queue()
    # p = Process(target=rungames, args=(q,))
    # p.start()
    # print(q.get())
    # p.join()
    print(f"Total time: {time.time()-start}")
    print(f"Margin of error: {max(results) - min(results)}\nHigh:\t{max(results)}\nLow:\t{min(results)}")