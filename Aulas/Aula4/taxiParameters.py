import random

class taxiParameters():
    def __init__(self, name):
        self.name = name 
        self.pos_x = random.uniform(0, 100)
        self.pos_y = random.uniform(0, 100)
        self.available = True