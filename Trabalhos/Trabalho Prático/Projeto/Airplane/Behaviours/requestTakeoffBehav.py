from spade.behaviour import OneShotBehaviour
from spade.message import Message
import asyncio
import random
from config import config
from messages import AirplaneInfo


class RequestTakeoffBehav(OneShotBehaviour):

    async def run(self):

        # Set new origin and destination
        self.agent.origin = config.cities[0]
        self.agent.destination = random.choice([city for city in config.cities if city != self.agent.origin])

        # Parked timer
        await asyncio.sleep(self.agent.parked_time)
        #print(str(self.agent.jid), "requesting takeoff permission...")

        # Request tower for takeoff permission
        msg = Message(to=f"tower@{config.host}")
        msg.set_metadata("performative", "request_takeoff")
        msg.body = AirplaneInfo(self.agent)
        await self.send(msg)
        self.agent.state = "waiting_takeoff_permission"