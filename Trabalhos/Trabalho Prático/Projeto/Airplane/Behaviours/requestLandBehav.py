from spade.behaviour import OneShotBehaviour
from spade.message import Message
from messages import AirplaneInfo
from config import config



class RequestLandBehav(OneShotBehaviour):
    
    async def run(self):

        #print(f"Airplane {self.agent.id} requesting to land")

        # Request landing to tower
        msg = Message(to=f"tower@{config.host}")
        msg.set_metadata("performative", "request_landing")
        msg.body = AirplaneInfo(self.agent)
        await self.send(msg)