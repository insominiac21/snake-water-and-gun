import random
import time
from pygame import mixer
mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()



lst = ("snake","water", "gun")

point_player = 0
point_comp = 0

print("\033[1;32;40m  \t\tWelcome to snake,water and gun game.\t\t")


name = str(input("\033[1;32;40m Please enter your name -> "))

chances =  int(input("\033[1;32;40m How many times do you wanna play? "))

while chances >0:
    time.sleep(1)
    
    print("Chances left",chances)
    time.sleep(1)
    choices =str(input("\033[1;34;40m \t What do you want to choose? \n 's' for snakes \n 'w' for water \n or'g' for gun \n ->  "))
    comp = random.choice(lst)
    
    
    #if player inputs S
    if choices == "s" and comp == "gun" :
        print('\033[1;36;40m oops you lost! \n your snake was hit by our gun!')
        chances-=1
        point_comp+=1
        
        
    elif choices == "s" and comp == "snakes":
        print("\033[1;37;40m It was a tie \n no chances were harmed \n and points to neither ")
    elif choices =="s" and comp == "water"    :
        print ("\033[1;35;40m You won! your snake dranked our water")
        chances-=1
        point_player+=1
    
    
    elif choices == "w" and comp == "snake" :
            print('\033[1;36;40m oops you lost! \n our snake dranked your water')
            chances-=1
            point_comp+=1
            
    elif choices == "w" and comp == "water":
        print("\033[1;37;40m It was a tie! \n no chances were harmed \n and points to neither ")
    elif choices =="w" and comp == "gun"    :

         print ("\033[1;35;40m You won! your water damaged our gun")
         chances-=1
         point_player+=1
         
    elif choices == "g" and comp == "water" :
            print('\033[1;36;40m oops you lost! \n your gun was damaged by our water')
            chances-=1
            point_comp+=1
            
    elif choices == "g" and comp == "gun":
        print("\033[1;37;40m It was a tie \n no chances were harmed \n and points to neither ")
    elif choices =="g" and comp == "gun":
        print ("\033[1;35;40m You won! your gun killed our snake, you monster!")
        chances-=1
        point_player+=1
    elif choices != "g":

        print('\033[1;30;40m inValid syntax \n please choose from g,s or w')
    
    elif choices != "s":
        print('\033[1;30;40m inValid syntax \n please choose from g,s or w')
    
    elif choices != "s" or "g" or "s":
        print('\033[1;30;40m inValid syntax \n please choose from g,s or w')
    
        

while chances==0:
    
    time.sleep(1)
    
    print('Gameover!')
    if point_player>point_comp:
        print('\033[1;31;40m Congrats,you are the winner')
    elif point_comp >point_player:
        print("\033[1;31;40m You lost,better luck next time")
    elif point_comp==point_player:
        print('\033[1;31;40m It was a tie! you were a tough competition')    
    
    time.sleep(1)       

    print('\033[1;33;40m Your score:',point_player)
    print('\033[1;33;40m Our score:',point_comp)
    
        
    exit()
         
#I am not able  restart the game....please help..I tried the folowing
# again= str(input('Do you want to play again? y/n '))
  #  while again== "y":
   #     chances+=10
    #    continue
     #   if again=="n":
      #      break
         





           
    