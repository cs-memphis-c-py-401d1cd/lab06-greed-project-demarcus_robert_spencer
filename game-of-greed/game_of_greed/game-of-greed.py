import random
import rolldice
import banker
import functools
from collections import Counter

class game_logic:
    def __init__(self,player,die):
        self.player = player
        self.die = []
    def calculate_score(self):
        pass
    def roll_dice(self):
        roll = random.choice(self.die)       
        return roll































    
"""def ran():
    rando = random.choice(die)
    print (rando) 
notTrue = True   
count = 0   
deiter = 6
def throwdice():
    while count <=len(die) and notTrue:
        for j in range(len(die)):
            
            res=input('please roll \n')
            
            if res.lower() == 'yes' or res.lower() == 'y':
                
                ran()
                
            else: break
                
        count +=1
        
        ask = input('would u like to roll again \n')
        
        if ask.lower()=='no' or ask.lower()=='n'or count == 6:
            
            notTrue = False
        """