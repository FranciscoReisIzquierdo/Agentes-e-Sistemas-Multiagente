from spade.behaviour import OneShotBehaviour
from spade.message import Message
from ...Aula4.customerParameters import customerParameters
import pickle

class requestTransport_Behav(OneShotBehaviour):

    async def run(self):

        self.agent.parameters = customerParameters(self.agent.jid)

        msg = Message(to="manager@msi")
        msg.set_metadata("performative", "customerRequestTransport")
        msg.body = self.agent.parameters
        serializedMessage = pickle.dumps(msg)
        await self.send(serializedMessage)
        print("Requested for taxi:", msg.body)