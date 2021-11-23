import sys
import os
import clearShelf
import bank
import shelf

class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    # shelf is the points that are available from picking the dice out
    # TODO: Implement method to add points to shelf/round
    def shelf():
        pass

    # after deciding not to roll anymore, those points are then tallied and banked for a total score
    # TODO: Implement method to add points to bank for game
    def bank():
        pass

    # reset points of round back to zero
    # TODO: Implement method to reset shelf/round pts back to zero
    def clear_shelf():
        pass 





def say_hello(name):
    print(f"hello, {name}!!")   