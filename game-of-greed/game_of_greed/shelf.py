from typing import List
from rolldice import dice

    # shelf is the points that are available from picking the dice out

def shelf():
      fakeList = [1,2,3,5,5,2]
      chosenPoints = []

      # we need to keep track of the points available and points chosen
      currentThrow = dice(fakeList)
      # what comprises our points, these point are still in a list of list when given to the variable
      pointBreakdown = [x for x in currentThrow if isinstance(x, list)]
      # what the points are quantified too, these points are still in a list when given to the variable
      availablePoints = [x for x in currentThrow if isinstance(x, int)][0]
      # i need to check for if there is 1 oor 5 available, or the ose their points, lets start at checking for ints 1 or 5
      

      numCheck5 = pointBreakdown.pop()
      numCheck1 = pointBreakdown.pop()

      try:
            if numCheck5 and numCheck1:
                  if len(numCheck5) > 0 and len(numCheck1) > 0:
                        print('I have cheked 1s and 5s')
                  elif len(numCheck5) > 0:
                        print('I checked only 5s')
                  elif len(numCheck1) > 0:
                        print('I checked only 1s')
                  else:
                        print('I found nothing in this throw')
            elif numCheck5:
                  if len(numCheck5) > 0:
                        print('I have cheked 5s')
                  else:
                        print('I could find no 5s')
            elif numCheck1:
                  if len(numCheck1) > 0:
                        print('I have cheked 1s')
                  else:
                        print('I could find no 1s')
            else:
                  print('I found no 1s or 5s')
      except:
            print(' The trees be blowin huh?')

      # I need to ask the user do they want to keep their current score available for that throw ONLY IF 1 or 5 is available
      
      #chosenNum = input(Which numbers would you like to keep)
      # IF they say no, continue rolling

      # If yes, take those dice out and roll with new total of dice


      

               
      print(pointBreakdown)
      # [[2, 2, 5, 1, 5, 2], [5, 5], [1]]

      print(f'You avalable points: {availablePoints}')
      # print(f'The numbers in the check for 1 or 5 was: {numCheckInitial}')

      # print(numCheck)


shelf()