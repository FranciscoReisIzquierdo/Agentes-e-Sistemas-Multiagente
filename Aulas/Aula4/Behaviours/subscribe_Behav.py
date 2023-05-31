import pickle
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from ...Aula4 import taxiParameters

class subscribe_Behav(OneShotBehaviour):

    async def run(self):
        self.agent.parameters = taxiParameters(self.agent.jid)

        msg = Message(to="manager@msi")
        msg.set_metadata("performative", "subscribeTaxi")
        msg.body = self.agent.parameters
        serializedMessage = pickle.dumps(msg)
        await self.send(serializedMessage)
        print("Subscribe taxi:", msg.body)