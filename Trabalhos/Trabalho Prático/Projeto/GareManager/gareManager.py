from spade import agent
import random
from config import config
from GareManager.Behaviours.listenBehav import ListenBehav

class Gare():
    def __init__(self, id, position, free):
        self.id = id
        self.position = position
        self.type = random.choice(config.airplane_types)
        self.free = free


def generateGares(n, occupied_gares):
    index = 0
    x, y = 0, 10
    points = []
    gares = []

    while len(points) < n:
        new_point = (random.uniform(x, y), random.uniform(x, y))
        if new_point not in points:
            points.append(new_point)
            gare = Gare(index, new_point, False) if index in occupied_gares else Gare(index, new_point, True)
            gares.append(gare)
            index += 1

    return gares


class GareManagerAgent(agent.Agent):

    def __init__(self, occupied_gares, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupied_gares = occupied_gares

    async def setup(self):
        
        print("Gare Manager Agent {}".format(str(self.jid)) + "starting...")
        self.gares = generateGares(config.num_gares, self.occupied_gares)

        self.add_behaviour(ListenBehav())