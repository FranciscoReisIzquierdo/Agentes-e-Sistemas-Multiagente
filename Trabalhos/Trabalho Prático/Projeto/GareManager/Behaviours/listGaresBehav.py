from spade.behaviour import OneShotBehaviour
from spade.message import Message
from messages import GaresInfo
from config import config


class ListGaresBehav(OneShotBehaviour):

    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data
    
    async def run(self):

        # Send gares to tower
        msg = Message(to=f"tower@{config.host}")
        msg.set_metadata("performative", "gares_list")
        msg.body = GaresInfo([g for g in self.agent.gares if g.type == self.data and g.free])
        await self.send(msg)