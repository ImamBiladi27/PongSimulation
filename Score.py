from threading import *
import Player

Score =0
PlayerXScore = 0
PlayerYScore = 0
obj1=Player.PlayerX()
obj2=Player.PlayerY()

ob=Player.Player1
ob2=Player.PlayerY

class score:




   def score1(self):
      print('Pemenangnya adalah player x')
   def score2(self):
      print('Pemenangnya adalah player y')


ex1 = score()
ex2 = score()

if(PlayerXScore==ob):
      t1=Thread(target=ex1.score1())
      t1.start()
      t1.join()
elif(PlayerYScore==ob2):
      t2=Thread(target=ex2.score2())
      t2.start()
      t2.join()





