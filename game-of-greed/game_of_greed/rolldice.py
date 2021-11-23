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
            # num = list(filter(lambda x: x%5==0, throw))
            num = [x for x in throw if x%5==0]
            numb = [x for x in throw if x<2]
            #function to reduce the lists 
            def reduced(arr):
                s=reduce(lambda a, b: a + b, arr)
                if s:
                    return s
                else:return arr[0]
                    
            #check for num and numb
            if num and numb:
                print('you have ones AND fives')
                s = reduced(num)
                sb = reduced(numb)
                sum = (s*10)+(sb*100)
                print(sum)
                #if they both occur check for each individually and 
                # check for each total number of times they occur 
                # then reduce those values to one value
            elif num:
                s = reduced(num)
                print(f'your number was reduced to {s*10}')    
                print('you have only fives')    
            elif numb:
                
                s = reduced(numb)
                print(f'your number was reduced to {s*100}')
                print('you have only ones')    
            else:print('you have no ones or no fives')    
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