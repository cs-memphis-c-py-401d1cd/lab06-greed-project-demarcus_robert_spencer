from rolldice import dice

def beginturn():
  arr = [1,2,3,4,5,6]
  container = []
  banked = []
  global choicebot
  player_dice_roll = dice(arr, container)
  throw = player_dice_roll[0]
  for x in throw:
    try:
        if x == 1 or x == 5 :
          choicebot = input ('Which die you like to keep? Choose in order from left to right starting with 0.')
        break
    except: continue
  split = choicebot.split(", ")
  for x in split:
    x = int(x)
    banked.append(throw[x])
  

  print(player_dice_roll)
  print(banked)
beginturn()



