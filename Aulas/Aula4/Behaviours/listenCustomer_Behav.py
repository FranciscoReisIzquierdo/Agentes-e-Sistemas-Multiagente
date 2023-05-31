import pickle
from spade.behaviour import OneShotBehaviour


class listenCustomer_Behav(OneShotBehaviour):

    async def run(self):
        while True:
            msg = await self.receive(timeout=1000)
            msg = pickle.load(msg)
            print("Message received with content: {}".format(msg.body))
            return