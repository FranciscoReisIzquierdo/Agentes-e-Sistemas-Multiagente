import random
from spade import agent

from Behaviours.makeRequest_Behav import MakeRequestBehav


class BuyerAgent(agent.Agent):

    async def setup(self):
        print("Agent {}".format(str(self.jid)) + "starting...")

        a = MakeRequestBehav(period=1)

        self.add_behaviour(a)