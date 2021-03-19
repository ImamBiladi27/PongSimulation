
import random
import copy
Player1=0
PLayer2=0
class Player(object):

    while Player1 <10 and PLayer2 <10:
        print("Player X")
        n = random.randint(0, 100)
        print(n)
        n2 = random.randint(0, 100)
        print("Player Y")
        print(n2)
        def thad1(self):
            print("Player X")

        if (n > 50 and n<100):
            print("Player X Tambah 1")
            Player1 += 1
            print('jumlahnya',Player1)

        def thad2(self):

            print("Player Y")

        if (n2 > 50 and n2<100):
            print("Player Y Tambah 1")
            PLayer2 += 1
            print('jumlahnya',PLayer2)


ex1=Player()
ex2=Player()
excopy=copy.deepcopy(ex1.thad1())
excopy2=copy.deepcopy(ex2.thad2())

class PlayerX(Player):
    pass

play=PlayerX()


class PlayerY(Player):
    pass

play=PlayerY()


