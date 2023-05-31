import random
from spade import agent
from spade.message import Message
from messages import AirplaneInfo
from Airplane.Behaviours.requestLandBehav import RequestLandBehav
from Airplane.Behaviours.requestTakeoffBehav import RequestTakeoffBehav
from Airplane.Behaviours.listenBehav import ListenBehav
from config import config


class AirplaneAgent(agent.Agent):

        def __init__(self, start_gare, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.start_gare = start_gare

        async def setup(self):
                self.landing_time = config.landing_time
                self.drive_time = config.drive_time
                self.parked_time = config.parked_time
                self.max_land_wait_time = config.max_land_wait_time
                
                self.id = self.jid
                self.destination = config.cities[0]
                self.origin = random.choice([city for city in config.cities if city != self.destination])
                self.company = random.choice(config.companies)
                
                self.add_behaviour(ListenBehav())

                if self.start_gare == None:
                        self.state = "on_air"
                        self.runway = None
                        self.gare = None
                        self.type = random.choice(config.airplane_types)
                        self.add_behaviour(RequestLandBehav())
                else:
                        self.state = "parked"
                        self.runway = None
                        self.gare = self.start_gare
                        self.type = self.start_gare.type
                        self.add_behaviour(RequestTakeoffBehav())

                #print("Airplane Agent {}".format(str(self.jid)) + "starting...")