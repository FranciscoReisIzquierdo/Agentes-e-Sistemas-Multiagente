import pickle
from spade import agent
from ..Aula4.Behaviours import listenManager_Behav

class ManagerAgent(agent.Agent):
    requests = []
    taxis = []

    
    async def setup(self):
        print("Agent {}".format(str(self.jid)) + "starting...")
        action = listenManager_Behav()
        self.add_behaviour(action)
        