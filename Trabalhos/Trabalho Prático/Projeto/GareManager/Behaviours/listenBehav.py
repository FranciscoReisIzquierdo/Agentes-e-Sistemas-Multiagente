from spade.behaviour import CyclicBehaviour
from messages import GareInfo
from spade.message import Message
from messages import GaresInfo
from GareManager.Behaviours.listGaresBehav import ListGaresBehav
from GareManager.Behaviours.changeGareBehav import ChangeGareBehav
from config import config

class ListenBehav(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=1000)
        type = msg.get_metadata("performative")

        if type == "list_gares":
            data = msg.body
            self.agent.add_behaviour(ListGaresBehav(data))
        
        elif type == "change_gare":
            data = GareInfo(msg.body)
            self.agent.add_behaviour(ChangeGareBehav(data))

        elif type == "request_report":
            msg = Message(to=f"admin@{config.host}")
            msg.set_metadata("performative", "response_report")
            msg.body = GaresInfo(self.agent.gares)
            await self.send(msg)