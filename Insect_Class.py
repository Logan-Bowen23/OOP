import random


class Insect:

    def __init__(self,n,w,l):
        self.name = n
        self.wings = w
        self.legs = l
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1,10)
        
    def get_miles(self):
        return self.flight

    def get_name(self):
        return self.name