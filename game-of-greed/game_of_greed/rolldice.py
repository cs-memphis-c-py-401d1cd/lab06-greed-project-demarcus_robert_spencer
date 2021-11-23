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
            #function to reduce the lists 
            def filtered(n):
                return [x for x in throw if x==n]
            def reduced(arr):
                s=reduce(lambda a, b: a + b, arr)
                if s:
                    return s
                else:return arr[0]
                
            num = filtered(5)
            numb = filtered(1)        
            #check for num and numb
            if num and numb:
                print('you have ones AND fives')
                s = reduced(num)
                sb = reduced(numb)
                sum = (s*10)+(sb*100)
                score += sum
                print(sum)
                #if they both occur check for each individually and 
                # check for each total number of times they occur 
                # then reduce those values to one value
            elif num:
                s = reduced(num)
                sa = s*10
                print(f'your number was reduced to {sa}')   
                score+=sa
                print('you have only fives')    
            elif numb:
                
                s = reduced(numb)
                sa = s*100
                print(f'your number was reduced to {sa}')   
                score+=sa
                print('you have only ones')    
            else:print('you have no ones or no fives')    
        except:print('your logic is messed up')    
        finally:print(f'score : {score}')
    except:print('what the fuvj')
    finally:print(throw)
