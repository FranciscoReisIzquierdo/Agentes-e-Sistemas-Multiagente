from spade.behaviour import PeriodicBehaviour
from spade.message import Message
import random

class MakeRequestBehav(PeriodicBehaviour):

    async def run(self):
        msg = Message(to="seller@192.168.56.1")
        msg.set_metadata("performative", "inform")
        msg.body = f"{random.randint(0, 6)}|{random.randint(1, 5)}"
        await self.send(msg)
        print("Requested:", msg.body)