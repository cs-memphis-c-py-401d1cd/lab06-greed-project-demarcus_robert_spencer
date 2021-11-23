import random
from functools import reduce

def dice(arr):
    #container to hold all die
    container = []
    # list to hold the random thrown dice
    throw = []
    #init score to zero
    score=0
    #loop through the list
    for i in arr:
        #append all the lists to a parent list
        container.append(arr)
        # set the group of lists to a variable 
    thrown = [i for i in container]       
    #  loop through the thrown list
    for i in thrown:
        #get a random number from each die
        ranint = random.choice(i)
        #append the random numbers to a list
        throw.append(ranint)
    try:
            #filter through the throw list for fives and again for ones
        try:    
            num = list(filter(lambda x: x == 5, throw))
            numb = list(filter(lambda x: x == 1, throw))
            total = reduce(lambda a, b: a + b, num)
            totalb = reduce(lambda a, b: a + b, numb)
            if total or totalb:
                print('you have ones and fives')
            elif total:
                print('you have fives')
            elif totalb:
                print('you have ones')
            else:print('i just cant wrap my head around it')
        except:print('your logic is messed up')    
        
        
        
        
        
        
        
        # if num and numb:
        #     s =functools.reduce(lambda a,b : a+b,num)
        #     sa =functools.reduce(lambda a,b : a+b,numb)
        # elif num:
        #     s =functools.reduce(lambda a,b : a+b,num)
        # elif numb:
        #     sa =functools.reduce(lambda a,b : a+b,numb)   
        # #filter the list of ones
        # if sa and s:
        #     score+=s*10+sa*100
        # elif s:
        #     score+=s*10
        # elif sa:
        #     score+=sa*100
        # else:return              
        # print(throw)
        # print(score)
    except:print('what the fuvj')
    finally:print(throw)
dice([1,2,3,4,5,6])