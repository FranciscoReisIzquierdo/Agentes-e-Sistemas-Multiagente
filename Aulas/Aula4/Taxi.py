import pickle
from spade import agent
from ..Aula4.Behaviours import subscribe_Behav, listenTaxi_Behav

class TaxiAgent(agent.Agent):

    parameters = None

    async def setup(self):
        print("Agent {}".format(str(self.jid)) + "starting...")
        subscribe = subscribe_Behav()
        self.add_behaviour(subscribe)

        trip = listenTaxi_Behav()
        self.add_behaviour(trip)