import random
from spade import agent
from Tower.Behaviours.listenBehav import ListenBehav
from config import config

class RunWay():
    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.free = True


def generateRunWays(n):
    index = 0
    x, y = 0, 10
    points = []
    runways = []

    while len(points) < n:
        new_point = (random.uniform(x, y), random.uniform(x, y))
        if new_point not in points:
            points.append(new_point)
            runWay = RunWay(index, new_point)
            runways.append(runWay)
            index += 1

    return runways


class TowerAgent(agent.Agent):

    def fastest_pair(self, gares):
        
        if len(gares) == 0: return None, None

        min_dist = 1000
        min_runway = None
        min_gare = None

        for runway in self.runways:
            if runway.free:
                for gare in gares:
                    dist = (runway.position[0] - gare.position[0]) ** 2 + (runway.position[1] - gare.position[1]) ** 2
                    if dist < min_dist:
                        min_dist = dist
                        min_runway = runway
                        min_gare = gare
        return min_runway, min_gare


    def add_plane(self, plane):
        self.planes[plane.id] = plane

    
    def remove_plane(self, plane):
        if plane.id in self.planes.keys():
            del self.planes[plane.id]

    def add_abort(self, plane):
        if len(self.aborts) > 3:
            self.aborts.pop(-1)
        self.aborts = [plane] + self.aborts

    async def setup(self):
        print("Control Tower Agent {}".format(str(self.jid)) + "starting...")

        self.runways = generateRunWays(config.num_runways)
        
        self.planes = {}
        self.aborts = []
        self.landing_queue = []
        self.takeoff_queue = []
        self.max_land_queue_size = config.max_land_queue_size

        self.add_behaviour(ListenBehav())